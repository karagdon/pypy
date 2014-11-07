try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'k8 48 Project',
    'author': 'k8',
    'url': 'myfakeworld.com',
    'download_url': 'myfakeworld.com/code',
    'author_email': 'me@myfakeworld.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'k848Project'
}

setup(**config)
