
"""
python module for installing and reading test data

fixture provides an interface for loading tabular data into
various storage media such as a database, CSV file, XML file, et
cetera. This is useful for testing and aims to solve this
common problem:

    You have a test that wants to work with lots of data and you
    need a way to easily reference that data when making assertions.

Note that this module is a rewrite of the fixtures interface
first distributed in http://testtools.python-hosting.com/

INSTALL
-------

from the root source directory:

    python setup.py install

or if you have the easy_install command:
    
    easy_install fixture

"""

__version__ = "1.0"