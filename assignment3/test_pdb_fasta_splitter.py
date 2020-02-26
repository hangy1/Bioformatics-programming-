#!/usr/bin/env python3
'''
Test suite for pdb_fasta_splitter.py
'''
import pytest
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
from pdb_fasta_splitter import (get_fh, get_header_and_sequence_lists,
                                _check_size_of_lists, _distinct_protein_secondary)

#global test variable
fh_in = open("test.txt", "r")
header_list_global = ['>101M:A:sequence', '>101M:A:secstr']
header_list_problem = ['>101M:A:sequence', '>101M:A:secstr', '>102M:A:secstr']
sequence_list_global = ['MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPET\
LEKFDRVKHLKTEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYL\
EFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKELGYQG','    HHHHHHHHHH\
HHHHGGGHHHHHHHHHHHHHHH GGGGGG TTTTT  SHHHHHH HHHHHHHHHHHHHHHHHHTTTT\
  HHHHHHHHHHHHHTS   HHHHHHHHHHHHHHHHHH GGG SHHHHHHHHHHHHHHHHHHHHHHHHTT   ']

def test_get_fh():
    fh_in = open("test.txt", "r")
    assert get_fh("test.txt", "r") == fh_in
    fh_out = open("out.txt", "w")
    assert get_fh("out.txt", "w") == fh_out

def test_get_header_and_sequence_lists():
    header_list, sequence_list = get_header_and_sequence_lists(fh_in)
    assert header_list == header_list_global
    assert sequence_list == sequence_list_global

def test_check_size_of_lists():
    with pytest.raises(SystemExit):
        _check_size_of_lists(header_list_problem, sequence_list_global)
    assert _check_size_of_lists(header_list_global, sequence_list_global)\
        == True

def test_distinct_protein_secondary():
     sec_str_header_list, protein_header_list = \
         _distinct_protein_secondary(header_list_global)
     assert sec_str_header_list == ['>101M:A:secstr']
     assert protein_header_list == ['>101M:A:sequence']