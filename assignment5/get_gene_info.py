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
    parser.add_argument('-host', dest='CLI1', \
                        help='Path to the file to open', required=False)
    parser.add_argument('-gene', dest='CLI2', \
                        help='Path to the gene category to open', required=False)
    return parser.parse_args()

#globa variable
keyword_dict = config.get_host_keywords()
scientific_name = keyword_dict.values()
common_name = keyword_dict.keys()
argvs = get_cli_args()
temp_host_name = argvs.CLI1
temp_gene_name = argvs.CLI2


def __print_scientific_name():
    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name\n")
    list_scietific = tuple(enumerate(set(scientific_name),1))
    for index, name in list_scietific:
        print("{}.\t{}".format(index, name.capitalize()))

def __print_common_name():
    print("\nHere is a (non-case sensitive) list of available Hosts by common name\n")
    list_common = tuple(enumerate(sorted(set(common_name)),1))
    for index, name in list_common:
        print("{}.\t{}".format(index, name.capitalize()))

def __print_host_directories():
    print('\nEither the Host Name you are searching for is not in the database\n\n\
or If you are trying to use the scientific name please put the name in double quotes:\n\n\
"Scientific name"')
    __print_scientific_name()
    __print_common_name()

def modify_host_name(temp_host_name):
    if temp_host_name is None:
        temp_host_name = "Homo_sapiens"
    else:
        temp_host_name = temp_host_name.lower()
        if temp_host_name in keyword_dict.keys():
            print(keyword_dict.get(temp_host_name))
            return keyword_dict.get(temp_host_name)
        else:
            __print_host_directories()

def get_gene_data(gene_name = "TGM1"):
    if temp_host_name is None:
        host_name = "Homo_sapiens"
        gene_name = "TGM1"
    else:
        host_name = modify_host_name(temp_host_name)
    file = "/".join((config.get_unigene_directory(), \
                     host_name,gene_name + "." + config.get_uigene_extension()))
    if my_io.is_valid_gene_file_name(file):
        # using f-strings
        print(f"\nFound Gene {gene_name} for {host_name}")
    else:
        print("Not found")
        print(f"Gene {gene_name} does not exist for {host_name}. exiting now...", file=sys.stderr)
        sys.exit()
    fh_in = my_io.get_fh(file,"r")
    for line in fh_in:
        match = re.search('^EXPRESS\s+(\D+)',line)
        if match:
            tissue_string = match.group(1)
            tissue_list = list(tissue_string.split(sep='|'))
            return tissue_list



def print_output(host_name ="Homo_sapiens",gene_name = "TGM1", \
                 tissue_list = get_gene_data("TGM1") ):
    tissues_number = len(tissue_list)
    print(f"\nIn {host_name}, There are {tissues_number} tissues that {gene_name} is expressed in:\n")
    for index, tissue in sorted(enumerate(tissue_list,1)):
        print(f"{index}.\t{tissue.capitalize()} ")

def main():
    host_name = modify_host_name(temp_host_name) if temp_host_name is not None else "Homo_sapiens"
    tissue_list = get_gene_data(temp_gene_name)
    print_output(host_name, temp_gene_name, tissue_list)

if __name__ == '__main__':
    main()