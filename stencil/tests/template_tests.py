'''
nose test suite for template module

To run some specific tests below use;
nosetests -w tests tests/stencil_tests.py:test_series_loader
'''



from nose.tools import *
from stencil import template





def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "Test basic"


def test_series_loader():
    print "Testing template"

    assert 1 == 1


