from setuptools import setup
from reqres import __version__

setup(
    name='reqres',
    version=__version__,
    py_modules=['reqres'],
    entry_points='''
        [console_scripts]
        reqres=reqres
    ''',
)
