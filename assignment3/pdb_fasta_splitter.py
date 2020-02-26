#!/usr/bin/env python3
'''
open file and generate two files. One with the corresponding protein sequence , \
and the other with the corresponding secondary structures
'''

import sys
import re
import argparse

def get_fh(file_name, ways_2_open):
    '''
    open the file name as the file handle
    :param file_name:
    :param ways_2_open:
    :return:
    '''
    try:
        handle = open(file_name, ways_2_open)
    except IOError:
        raise Exception("Error: File cannot be opened, please use the correct file")
    except ValueError:
        print('Error: Please choose to read ("r"), write ("w") or append("a") file')
        raise
    return handle

def get_header_and_sequence_lists(file_handle):
    '''
    take file handle and create list of sequences in the file
    and  list for the headers in the file
    :param file_handle:
    :return:
    '''
    header_list = []
    sequence_list = []
    single_seq = ''
    with file_handle as fh_in:
        for line in fh_in:
            line = line.strip("\n")
            # if the line is header,print out the line from second character
            if line.startswith(">"):
                header_list.append(line)
                sequence_list.append(single_seq)
                # reset single_set to a empty string
                single_seq = ""
            elif line != "":
                single_seq += line
    # add the last sequence to sequence_list
    # and then delete the first blank seuquence in the list
    sequence_list.append(single_seq)
    sequence_list = list(filter(lambda x: x != "", sequence_list))
    _check_size_of_lists(sequence_list, header_list)
    # exit system if the list lengths are not equal
    return header_list, sequence_list

def _check_size_of_lists(list_headers, list_seqs):
    '''
    check if the number of headers in the list_header
    is the same as sequences in the list_seqs
    :param list_headers:
    :param list_seqs:
    :return:
    '''
    if len(list_headers) != len(list_seqs):
        sys.exit("The size of the sequences and the header lists is different\n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def _distinct_protein_secondary(list_headers, list_sequences):
    '''
    take list_headers and separate it into two lists, one for
    headers of protein sequences, another for headers of secondary
    structure sequences
    :param list_headers:
    :return:
    '''
    protein_list = []
    sec_str_list = []
    count_protein = 0
    count_sec_str = 0
    for header,seq in zip(list_headers, list_sequences):
        if re.search(r"secstr", header):
            count_sec_str += 1
            sec_str_list.append(header)
            sec_str_list.append(seq)
        elif re.search(r"sequence", header):
            count_protein += 1
            protein_list.append(header)
            protein_list.append(seq)
    return count_sec_str, count_protein, sec_str_list, protein_list


def get_cli_args():
    '''
    set up parser for command line, one argument is added
    :return:
    '''
    parser = argparse.ArgumentParser(description='Give \
    the fasta sequence file name to do the splitting')
    parser.add_argument('-i', '--infile', dest='INFILE', \
                        help='Path to the file to open', required=True)
    return parser.parse_args()

def main():
    '''
    define input and output files and print statements
    :return:
    '''
    argvs = get_cli_args()
    in_file = argvs.INFILE
    fh_in = get_fh(in_file, "r")
    list_headers, list_sequences = get_header_and_sequence_lists(fh_in)
    count_sec_str, count_protein, sec_str_list, protein_list = _distinct_protein_secondary(list_headers, list_sequences)
    fh_out_sec_str = get_fh("pdb_ss.fasta", "w")
    fh_out_protein = get_fh("pdb_protein.fasta", "w")
    print(*sec_str_list, sep='\n', file=fh_out_sec_str)
    print(*protein_list, sep='\n', file=fh_out_protein)
    print("Found {} protein sequences\nFound {} ss sequences".\
          format(count_protein, count_sec_str))
    fh_out_protein.close()
    fh_out_sec_str.close
if __name__ == '__main__':
    main()
