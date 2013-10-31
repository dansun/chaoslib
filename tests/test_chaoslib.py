# -*- coding: utf-8 -*-

from nose import with_setup
from unittest import TestCase
import chaoslib

class Test_chaoslib(TestCase):
    """
        Testing all defined functions in the chaoslib.
    """

    #
    # Define setup and teardown for classes and methods
    #
    def setup():
        print('Setup...')

    def teardown():
        print('Teardown...')

    #
    # Define testcases for chaoslib
    #
    @with_setup(setup, teardown)
    def test_default_sorting(testcase):
        assert chaoslib.sort([3, 2, 1]) == [1, 2, 3]

    @with_setup(setup, teardown)
    def test_custom_sorting(testcase):
        assert chaoslib.sort([3, 1, 2], lambda x,y: x<=y) == [3, 2, 1]
        assert chaoslib.sort([3, 1, 2], lambda x,y: x>=y) == [1, 2, 3]

    @with_setup(setup, teardown)
    def test_default_is_sorted(testcase):
        assert chaoslib.is_sorted([1, 2, 3]) is True
        assert chaoslib.is_sorted([3, 2, 1]) is False

    @with_setup(setup, teardown)
    def test_custom_is_sorted(testcase):
        assert chaoslib.is_sorted([1, 2, 3], lambda x,y: x>=y) is True
        assert chaoslib.is_sorted([3, 2 ,1], lambda x,y: x>=y) is False
        assert chaoslib.is_sorted([1, 2, 3], lambda x,y: x<=y) is False
        assert chaoslib.is_sorted([3, 2 ,1], lambda x,y: x<=y) is True
        