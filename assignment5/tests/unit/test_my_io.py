#!/usr/bin/env python3

"""Test suite for module my_io.py"""
import os
import pytest
from assignment5 import my_io

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

FILE_2_TEST = "test.txt"
def _create_test_file(file):
    open(file, "w").close()

def test_is_valid_gene_file_name():
    _create_test_file(FILE_2_TEST)
    assert my_io.is_valid_gene_file_name(FILE_2_TEST) == True, "Not valid file"
    os.remove(FILE_2_TEST)

def test_existing_get_fh_4_reading():
    _create_test_file(FILE_2_TEST)
    test = my_io.get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") == True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)

def test_existing_get_fh_4_writing():
    test = my_io.get_fh(FILE_2_TEST, "w")
    assert hasattr(test, "write") == True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)

def test_get_fh_4_ValueError():
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        my_io.get_fh("test.txt", "rrr")
        os.remove(FILE_2_TEST)

def test_get_fh_4_TypeError():
    _create_test_file(FILE_2_TEST)
    with pytest.raises(TypeError):
        my_io.get_fh([], "r")
    os.remove(FILE_2_TEST)

def test_get_fh_4_OSError():
    _create_test_file(FILE_2_TEST)
    with pytest.raises(OSError):
        my_io.get_fh("does_not_exist.txt", "r")
    os.remove(FILE_2_TEST)
