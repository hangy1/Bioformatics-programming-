import sys
import argparse
from assignment4 import my_io


def file_2_genesdict(infile):
    '''
    Extract content from a text file to a dictionary
    '''
    dict_genes = dict()
    fh_in1 = my_io.get_fh(infile, "r")
    for line in fh_in1:
        line = line.strip()
        gene_symbol, gene_desc = line.split('\t')[0:2]
        gene_category = line.split('\t')[2] if len(line.split('\t')) is 3 else "Other"
        # print("{}\t{}\t{}".format(gene_symbol, gene_desc, gene_category))
        dict_genes.update({gene_symbol: [gene_desc, gene_category]})
    return dict_genes


def match_gene(gene_symbol, dict_genes):
    '''
    find the input gene symbol in genes dictionary
    '''
    for key in dict_genes.keys():
        if gene_symbol.upper() == key.upper():
            print("{} fount! Here is the description: {}".format(key, dict_genes[key][0]))
    if gene_symbol == "QUIT":
        sys.exit("Thanks for querying the data.")
    elif gene_symbol.upper() not in [key.upper() for key in dict_genes.keys()]:
        print("Not a valid gene name.")


def get_cli_args():
    '''
    set up parser for command line, two argument are added
    :return:
    '''
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, \
    and ask user for a gene name')
    parser.add_argument('-i', '--infile', dest='INFILE', \
                        help='Path to the file to open', required=True)
    return parser.parse_args()


def main():
    '''
    take interactive input as gene_symbol and find the matching description
    '''
    argvs = get_cli_args()
    in_file = argvs.INFILE
    print("Enter gene name of interest. Type quit to exit:")
    gene_symbol = input('')
    dict_genes = file_2_genesdict(in_file)
    match_gene(gene_symbol, dict_genes)


if __name__ == '__main__':
    main()
