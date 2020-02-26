#!/usr/bin/env python3
'''
print the number of A's, T's, G's, C's, N's, length of the sequence and \
also the %GC content of the entire sequence for each sequences in file
'''

import re
import warnings
import argparse
from pdb_fasta_splitter import (get_fh, get_header_and_sequence_lists)
# ignore all "Variable name doesn't conform to snake_case naming style (invalid-name)
# pylint: disable=C0103

def _get_nt_occurrence(character, sequence):
    '''
    count the character in the string
    :param character:
    :param sequence:
    :return:
    '''
    count_char = sequence.count(character)
    return count_char


def _get_accession(header_string):
    '''
    extract accession number from full header line
    :param header_string:
    :return:
    '''
    # find the pattern that matches accession number, which starts from\
    # '<', followed by letters, and end with numbers
    extracted_accession = re.findall(r">\w+\d+", header_string)
    accession_string = (extracted_accession[0])[1:]
    return accession_string


def _get_sequence_stats(header, sequence):
    '''
    obtain the statistic analysis for one header and sequence
    and make a string of it
    :param header:
    :param sequence:
    :return:
    '''
    accession_string = _get_accession(header)
    num_As = _get_nt_occurrence("A", sequence)
    num_Gs = _get_nt_occurrence("G", sequence)
    num_Cs = _get_nt_occurrence("C", sequence)
    num_Ts = _get_nt_occurrence("T", sequence)
    num_Ns = _get_nt_occurrence("N", sequence)
    seq_length = len(sequence)
    gc_content = (num_Gs + num_Cs) / seq_length
    sequence_stats_string = " {}\t\t{}\t{}\t{}\t{}\t{}\t{}\t{:10.2f}".format \
        (accession_string, num_As, num_Gs, num_Cs, \
         num_Ts, num_Ns, seq_length, gc_content)
    return sequence_stats_string


def print_sequence_stats(list_headers, list_sequences, fh_out):
    '''
    print header line, add number(index) to sequence_stats_string\
    and print them to a output file handle
    :param list_headers:
    :param list_sequences:
    :param fh_out:
    :return:
    '''
    list_sequence_stats = []
    name_list = ["Number", "Accession", "A's", "G's", "C's", \
                 "T's", "N's", "Length", "GC_content"]
    header_line = "\t".join(name_list)
    list_sequence_stats.append(header_line)
    # add index at the very front of each sequence_stats_string
    for index, (header, sequence) in enumerate(zip(list_headers, list_sequences),start=1):
        sequence_stats_string = _get_sequence_stats(header, sequence)
        sequence_stats_string = '{}\t{}'.format(index, sequence_stats_string)
        list_sequence_stats.append(sequence_stats_string)
    _check_size_of_stats_lists(list_headers, list_sequence_stats)
    print(*list_sequence_stats, sep='\n', file=fh_out)


def _check_size_of_stats_lists(list_headers, list_sequence_stats):
    '''
    check if list_headers equals to to total sequence_stats_string
    :param list_headers:
    :param list_sequence_stats:
    :return:
    '''
    #substract the header line in list_sequence_stats
    if len(list_headers) != len(list_sequence_stats) - 1:
        warnings.warn("Not all the sequences are being analyzed!")
    else:
        return True


def get_cli_args():
    '''
    set up parser for command line, two argument are added
    :return:
    '''
    parser = argparse.ArgumentParser(description='Give the fasta \
    sequence file name to get the nucleotide statistics')
    parser.add_argument('-i', '--infile', dest='INFILE', \
                        help='Path to the file to open', required=True)
    parser.add_argument('-o', '--outfile', dest='OUTFILE', \
                        help='Path to the file to open', required=True)
    return parser.parse_args()


def main():
    '''
    define input and output files and, write final output to a file handle
    :return:
    '''
    argvs = get_cli_args()
    in_file = argvs.INFILE
    out_file = argvs.OUTFILE
    fh_in = get_fh(in_file, "r")
    list_headers, list_sequences = get_header_and_sequence_lists(fh_in)
    fh_out = get_fh(out_file, "w")
    print_sequence_stats(list_headers, list_sequences, fh_out)
    fh_out.close()

if __name__ == '__main__':
    main()
