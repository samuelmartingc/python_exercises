try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My project',
    'author' : 'My name',
    'url' : 'url to get it at',
    'download_url' : 'where to download it',
    'author_email' : 'My email',
    'version' : '0.0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
