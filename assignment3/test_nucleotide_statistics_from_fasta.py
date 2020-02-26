#!/usr/bin/env python3
'''
Test suite for nucleotide_statistics_from_fasta.py
'''
import pytest
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
from nucleotide_statistics_from_fasta import \
    (_get_nt_occurrence, _get_accession, _get_sequence_stats)

def test_get_nt_occurrence():
    assert _get_nt_occurrence("A", "ACCTAGCN") == 2
    assert _get_nt_occurrence("C", "ACCTAGCN") == 3

def test_get_accession():
    assert _get_accession('>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)')\
        == 'EU521893'
    assert _get_accession('>U71147 A/Miyagi/29/95 1995// 5 (NP)') == 'U71147'

def test_get_sequence_stats():
    header = '>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)'
    sequence = 'AACAGCACGGC'
    assert _get_sequence_stats(header, sequence) == \
           ' EU521893\t\t4\t3\t4\t0\t0\t11\t0.64'

