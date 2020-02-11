#!/usr/bin/env python3
#calc_numbers_amino_acid.py.py

import sys

name = input("Please enter a name for the DNA sequence : ")
print("Your sequence name is:",name)

dna_len = input("please enter the length of the sequence: ")
print("The length of DNA sequence is",dna_len)
if dna_len != int:
    raise Exception("sequence length must be integer")

#calculate the length of decoded protein, exit if DNA sequence is not multiple of 3. 
protein_len = int(dna_len)/3
if int(dna_len) % 3 == 0:
    print("The length of the decoded protein is:",protein_len) 
    weight = int(protein_len) * 110 / 1000
    print("The average weight of the protein sequence is {:.2f}".format(weight))
else:
    sys.exit("ERROR:the DNA sequence is not a multiple of 3")


