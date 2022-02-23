"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ThunderThings.py']
DATA_FILES = []
OPTIONS = dict(
    plist=dict(
        LSEnvironment=dict(
            APPLAUNCHED='Y',
        )
    )
)
    
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)