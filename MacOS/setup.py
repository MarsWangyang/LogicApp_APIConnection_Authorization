"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

lib_list = []
with open('./requirements_macos.txt', 'r') as f:
    line = f.readline()
    while(line):
        line = f.readline().split("==")[0]
        lib_list.append(line)

APP = ['main.py']
DATA_FILES = ['.env']
OPTIONS = {
    'plist': {'includes': lib_list}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)