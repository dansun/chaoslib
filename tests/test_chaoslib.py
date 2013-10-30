# -*- coding: utf-8 -*-
from nose import with_setup
from unittest import TestCase
import chaoslib

class Test_chaoslib(TestCase):
    #
    # Define setup and teardown for classes and methods
    #
    def setup():
        print('Setup.')

    def teardown():
        print('Teardown.')

    #
    # Define tests for chaoslib
    #
    @with_setup(setup, teardown)
    def test_sort(testcase):
        mylist = [1,2,3]
        assert chaoslib.sort(mylist) != mylist

