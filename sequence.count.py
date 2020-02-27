#!/usr/bin/env python3

#set empty list and initial count
headers = []
numbers = []
count = 0

with open ("yeast.fasta", "r") as f:
    for line in f: 
        line = line.strip()
        #if the line is header,print out the line from second character 
        if line[0] == ">":
            headers.append(line[1:])
            #append count of the previous sequence, and initial count again 
            if count != 0:
                numbers.append(count)
                count == 0
            else:
                continue
        #if the line is sequence line, count it until the next header line
        else:
            count = count + len(line)
#append the last sequence count
numbers.append(count)

#print values from each lists
for header, number in zip(headers, numbers):
    print("{}\t{}".format(header, number))
