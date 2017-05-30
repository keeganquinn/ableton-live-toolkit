from setuptools import setup, find_packages
from live_toolkit import cmd

setup(
    name='live_toolkit',
    version=cmd.__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ableton-tool = live_toolkit.cmd:main'
        ],
    },
    install_requires=open('requirements.txt').readlines(),

    description='Ableton Live Toolkit',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],

    author='Colour Code',
    author_email='colour-code@live.com',
)
