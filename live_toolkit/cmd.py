"""Ableton Live Toolkit

Usage:
  ableton-tool decompile-midi-remote-scripts [<dst>]
  ableton-tool (-h | --help)
  ableton-tool --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""


import shutil
import platform
import os

from docopt import docopt
from uncompyle6 import uncompyle_file

__version__ = "0.0.1"


class CouldNotFindAppResourcesDirectory(Exception):
    """Exception raised when no Live installation can be found."""
    pass


class UMad(Exception):
    """Having a laugh, are we?"""
    pass


def get_ableton_resources_directory():
    """Locate and return the path to the installed Live resources directory."""
    possible_dirs = []

    if platform.system() == "Darwin":
        possible_dirs = [
            "/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/"
        ]
    elif platform.system() == "Linux":
        print "U MAD? Ableton on Linux?!"
        raise UMad
    elif platform.system() == "Windows":
        possible_dirs = [
            # XXX fill me in. I don't have winzoz..
        ]

    for path in possible_dirs:
        if os.path.isdir(path):
            return path

    raise CouldNotFindAppResourcesDirectory


def decompile_midi_remote_scripts(output_dir):
    """Decompile all MIDI Remote Scripts from the installed Live."""
    midi_remote_dir = os.path.join(get_ableton_resources_directory(),
                                   "MIDI Remote Scripts")

    for root, dirs, files in os.walk(midi_remote_dir):
        for dirname in dirs:
            dir_src = os.path.join(root, dirname)
            dir_dst = os.path.join(
                output_dir, dir_src.replace(
                    midi_remote_dir + os.path.sep, ""))
            if not os.path.isdir(dir_dst):
                os.makedirs(dir_dst)

        for filename in files:
            file_src = os.path.join(root, filename)
            file_dst = os.path.join(
                output_dir, file_src.replace(
                    midi_remote_dir + os.path.sep, ""))
            if filename.endswith(".pyc"):
                file_dst = file_dst.replace(".pyc", ".py")
                print "Decompiling %s into %s" % (file_src, file_dst)
                outstream = open(file_dst, "w+")
                uncompyle_file(file_src, outstream)
                outstream.close()
            else:
                shutil.copyfile(file_src, file_dst)


def main():
    """Main program function."""
    args = docopt(__doc__, version='Ableton Live Toolkit ' + __version__)
    if args['decompile-midi-remote-scripts']:
        target_dir = "MIDI Remote Scripts"
        if args['<dst>']:
            target_dir = args['<dst>']
        decompile_midi_remote_scripts(target_dir)
