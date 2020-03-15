import argparse
import os.path
from assignment4 import my_io

def set_genes(infile):
    """
    extract genes ID into a set
    """
    set_geneid = set()
    fh_in = my_io.get_fh(infile, "r")
    # skip the header line
    next(fh_in)
    for line in fh_in:
        line = line.strip()
        gene_id = line.split("\t")[0]
        set_geneid.add(gene_id)
    return set_geneid


def get_common_gene(set_genes1, set_genes2):
    """
    obtain common genes from two gene sets
    """
    set_common_gene = set_genes1.intersection(set_genes2)
    sort_common_gene = sorted(set_common_gene)
    return sort_common_gene


def get_cli_args():
    """
    set up parser for command line, two argument are added
    :return:
    """
    parser = argparse.ArgumentParser(description='Combine on gene name \
    and count the category occurrence')
    parser.add_argument('-i1', '--infile1', dest='INFILE1', \
                        help='Gene list 1 to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='INFILE2', \
                        help='Gene list 2 to open', required=True)
    return parser.parse_args()


def main():
    """
    print stdout and write output file
    """
    argvs = get_cli_args()
    infile1 = argvs.INFILE1
    infile2 = argvs.INFILE2
    set_genes1 = set_genes(infile1)
    set_genes2 = set_genes(infile2)
    common_genes = get_common_gene(set_genes1, set_genes2)
    # write common genes to a output file
    out_path = os.path.join("./OUTPUT", "intersection_output.txt")
    fh_out = my_io.get_fh(out_path, "w")
    fh_out.writelines("{}\n".format(genes) for genes in common_genes)
    # print statements
    print("Number of unique gene names in {}: {}".format(infile1, len(set_genes1)))
    print("Number of unique gene names in {}: {}".format(infile2, len(set_genes2)))
    print("Number of common gene symbols found: {}".format(len(common_genes)))
    print("Output stored in {}".format(out_path))


if __name__ == '__main__':
    main()
