"""
py2app setup script for ABC+ Converter
Build with: python setup.py py2app
"""

from setuptools import setup

APP = ['app.py']
APP_NAME = 'ABC+ Converter'

DATA_FILES = [
    ('templates', ['templates/index.html']),
    ('static', ['static/style.css', 'static/script.js', 'static/abcjs-basic-min.js', 'static/opensheetmusicdisplay.min.js', 'static/manifest.json', 'static/sw.js']),
    ('static/icons', [
        'static/icons/icon-72.png',
        'static/icons/icon-96.png',
        'static/icons/icon-128.png',
        'static/icons/icon-144.png',
        'static/icons/icon-152.png',
        'static/icons/icon-192.png',
        'static/icons/icon-384.png',
        'static/icons/icon-512.png',
    ]),
    ('abc2xml', [
        'abc2xml/abc2xml.py',
        'abc2xml/LICENSE',
        'abc2xml/README.md',
    ]),
    ('', ['annotationguide.json']),
]

OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'AppIcon.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleIdentifier': 'com.abcplus.converter',
        'CFBundleVersion': '1.4.0',  # Keep in sync with APP_VERSION in app.py
        'CFBundleShortVersionString': '1.4.0',  # Keep in sync with APP_VERSION in app.py
        'LSMinimumSystemVersion': '10.13',
        'NSHighResolutionCapable': True,
    },
    'packages': ['flask', 'jinja2', 'werkzeug', 'markupsafe', 'click', 'itsdangerous', 'blinker', 'pyparsing', 'xml'],
    'includes': ['re', 'json', 'subprocess', 'tempfile', 'datetime', 'os', 'sys', 'xml.etree.ElementTree', 'xml.etree.cElementTree'],
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
