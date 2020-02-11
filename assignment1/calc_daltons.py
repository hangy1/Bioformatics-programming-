#!/usr/bin/env python3
#calc_daltons.py

import re

#create a loop to add the length of each line in fasta file 
count = 0
with open("rattus.fasta",'r')as f:
    for line in f.readlines():
        if re.match('^[A-Z]', line):
            line = line.replace('\r', '').replace('\n', '')
            count = count+len(line)
#calculate the total weight in kilodaltons
weight = count*110/1000

print('The length of "Protein kinase C beta type" is:{}\nThe average weight of this protein sequence in kilodaltons is:{}'.format(count,weight))

