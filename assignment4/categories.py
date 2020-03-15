import argparse
import collections
import re
import os.path
from operator import itemgetter
from assignment4 import my_io


def count_occur(infile1):
    """
    extract gene category from a file and count the occurrence of the categories
    """
    list_cate = []
    fh_in1 = my_io.get_fh(infile1, "r")
    for line in fh_in1:
        line = line.strip()
        category = line.split('\t')[2] if len(line.split('\t')) is 3 else "Other"
        if re.match(r'^\d', str(category)):
            list_cate.append(category)
    occur_dict = collections.Counter(list_cate)
    return occur_dict


def file_2_cate_dict(infile2):
    """
    convert a table text file into a dictionary
    """
    cate_dict = dict()
    fh_in2 = my_io.get_fh(infile2, "r")
    for line in fh_in2:
        line = line.strip("\n")
        cate_id, cate_desc = line.split('\t')
        cate_dict.update({cate_id: cate_desc})
    return cate_dict


def match_2_files(infile1, infile2):
    """
    Match categories and its occurrence with category description
    """
    occur_dict = count_occur(infile1)
    cate_dict = file_2_cate_dict(infile2)
    list_cate_desc = []
    for key, value in occur_dict.items():
        cate_string = '{}\t\t{}'.format(key, value)
        if key in cate_dict.keys():
            cate_string += "\t\t{}".format(cate_dict.get(key))
            list_cate_desc.append(cate_string)
    # sort with ascending category number
    sorted_cate_desc = sorted(list_cate_desc, key=itemgetter(0))
    # insert header line
    name_list = ["Category", "Occurrence", "Description"]
    header_line = "\t".join(name_list)
    sorted_cate_desc.insert(0, header_line)
    return sorted_cate_desc


def get_cli_args():
    """
    set up parser for command line, two argument are added
    :return:
    """
    parser = argparse.ArgumentParser(description='Combine on gene name \
    and count the category occurrence')
    parser.add_argument('-i1', '--infile1', dest='INFILE1', \
                        help='Path to the file to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='INFILE2', \
                        help='Path to the gene category to open', required=True)
    return parser.parse_args()


def main():
    """
    obtain sorted categories lists with description and write to a output file
    """
    out_path = os.path.join("./OUTPUT", "categories.txt")
    fh_out = my_io.get_fh(out_path, "w")
    argvs = get_cli_args()
    infile1 = argvs.INFILE1
    infile2 = argvs.INFILE2
    sorted_cate_desc = match_2_files(infile1, infile2)
    fh_out.writelines("{}\n".format(categories) for categories in sorted_cate_desc)


if __name__ == '__main__':
    main()
