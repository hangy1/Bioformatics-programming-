import sys
import re
import argparse
import warnings

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

