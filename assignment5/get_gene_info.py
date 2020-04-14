#!/usr/bin/env python3

"""
query the tissue expression for a given gene and species
"""

import argparse
import sys
import re
from assignment5 import config
from assignment5 import my_io


def get_cli_args():
    """
    set up parser for command line, two argument are added
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', dest='HOST', \
                        help='Please specify species name', required=False)
    parser.add_argument('-gene', dest='GENE', \
                        help='Please specify gene name', required=False)
    return parser.parse_args()


def __print_scientific_name():
    '''
    print scientific names when the file cannot be opened
    :return:
    '''
    keyword_dict = config.get_host_keywords()
    scientific_name = keyword_dict.values()
    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name\n")
    list_scietific = tuple(enumerate(set(scientific_name), 1))
    for index, name in list_scietific:
        print("{}.\t{}".format(index, name.capitalize()))


def __print_common_name():
    '''
    print common names when the file cannot be opened

    :return:
    '''
    keyword_dict = config.get_host_keywords()
    common_name = keyword_dict.keys()
    print("\nHere is a (non-case sensitive) list of available Hosts by common name\n")
    list_common = tuple(enumerate(sorted(set(common_name)), 1))
    for index, name in list_common:
        print("{}.\t{}".format(index, name.capitalize()))


def __print_host_directories():
    '''
    print statement when the file cannot be opened
    :return:
    '''
    print('\nEither the Host Name you are searching for is not in the database\n\n\
or If you are trying to use the scientific name please put the name in double quotes:\n\n\
"Scientific name"')
    __print_scientific_name()
    __print_common_name()


def modify_host_name(temp_host_name):
    '''
    modify input common name to scientific name
    :param temp_host_name:
    :return:
    '''
    keyword_dict = config.get_host_keywords()
    if temp_host_name is None:
        temp_host_name = "Homo_sapiens"
    else:
        temp_host_name = temp_host_name.lower()
        if temp_host_name in keyword_dict.keys():
            return keyword_dict.get(temp_host_name)
        else:
            __print_host_directories()
            sys.exit()


def get_gene_data(gene_name):
    '''
    extract expressed tissues list given by the gene name
    :param gene_name:
    :return:
    '''
    argvs = get_cli_args()
    temp_host_name = argvs.HOST
    if temp_host_name is None:
        host_name = "Homo_sapiens"
        gene_name = "TGM1"
    else:
        host_name = modify_host_name(temp_host_name)
    file = "/".join((config.get_unigene_directory(), \
                     host_name, gene_name + "." + config.get_uigene_extension()))
    if my_io.is_valid_gene_file_name(file):
        # using f-strings
        message = f"\nFound Gene {gene_name} for {host_name}"
    else:
        message = f"Not found\n\
        Gene {gene_name} does not exist for {host_name}. exiting now..."
        sys.exit()
    fh_in = my_io.get_fh(file, "r")
    for line in fh_in:
        match = re.search(r'^EXPRESS\s+(\D+)', line)
        if match:
            tissue_string = match.group(1)
            temp_tissue_list = list(tissue_string.split(sep='|'))
            tissue_list = sorted([tissue.strip() for tissue in temp_tissue_list])
            return message, tissue_list


def print_output(host_name="Homo_sapiens", gene_name="TGM1", \
                 tissue_list=get_gene_data("TGM1")):
    '''
    print expressed tissues with index, define the defaut values
    :param host_name:
    :param gene_name:
    :param tissue_list:
    :return:
    '''
    tissues_number = len(tissue_list)
    print(f"In {host_name}, There are {tissues_number} tissues that {gene_name} is expressed in:\n")
    for index, tissue in sorted(enumerate(tissue_list, 1)):
        print(f"{index}. {tissue.capitalize()} ")


def main():
    '''
    main
    :return:
    '''
    argvs = get_cli_args()
    temp_host_name = argvs.HOST
    temp_gene_name = argvs.GENE
    host_name = modify_host_name(temp_host_name) if temp_host_name is not None else "Homo_sapiens"
    message, tissue_list = get_gene_data(temp_gene_name)
    print(message)
    print_output(host_name, temp_gene_name, tissue_list)


if __name__ == '__main__':
    main()
