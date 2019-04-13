"""judge0api - A Python API for interacting with the Judge0"""


from . import language, submission
from .client import Client

__version__ = '0.1.14'
__author__ = 'Aaron Walker <aaw13@aber.ac.uk>'
__all__ = ['client', 'submission', 'language']

if __name__ == '__main__':
    pass
