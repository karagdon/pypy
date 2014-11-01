try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'K8 Project',
    'author': 'K8',
    'url': 'URL tbd.',
    'download_url': 'download it at TBD.',
    'author_email': 'My email is TBD.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'k8Proj'
}

setup(**config)