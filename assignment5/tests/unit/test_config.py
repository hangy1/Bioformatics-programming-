#!/usr/bin/env python3

"""Test suite for module config.py"""
import os
import pytest
from assignment5 import config

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

def test_get_error_string_4_unable_to_open(capfd):
    config.get_error_string_4_unable_to_open("test.txt", "r")
    out, err = capfd.readouterr()
    assert out == "Could not open the file: test.txt for type 'r'\n"

def test_get_error_string_4_ValueError(capfd):  # error when used get_fh(file, "1234")
    config.get_error_string_4_ValueError()
    out, err = capfd.readouterr()
    assert out == "Invalid argument Value for opening a file for reading/writing\n"


def test_get_error_string_4_TypeError(capfd):  # error when used get_fh(file, "r", "w")
    config.get_error_string_4_TypeError()
    out, err = capfd.readouterr()
    assert out == "Invalid argument Type\n"

def test_get_file_keywords():
    test = config.get_host_keywords()
    assert test.get("bos taurus") == "Bos_taurus"
    assert test.get("rats") == "Rattus_norvegicus"
    assert len(test.keys()) == 18
