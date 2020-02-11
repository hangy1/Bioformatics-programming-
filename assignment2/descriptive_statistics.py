#!/usr/bin/env python3
#descriptive_statistics.py

import sys
import math

def main():
    """
    main function to complete simple statistical analysis for every column in
    the txt file
    """
    count_line = 0
    column_to_parse = []
    with open(sys.argv[1], "r") as in_file:
        for line in in_file:
            count_line = count_line + 1
            try:
                num = line.split("\t")[int(sys.argv[2])]
            except IndexError: #int(sys.argv[2])<0 or column_num < int(sys.argv[2])
                print('Exiting: There is no valid "list index" in column {} in line {}\
 in file: {}'.format(sys.argv[2], count_line, sys.argv[1]))
                sys.exit(1)
            try:
                column_to_parse.append(float(num))
            except ValueError:
                print("Skipping line number {} : could not convert string to float\
:'{}'\n".format(count_line, num))

    #create a new list that store all the real numbers
    column_to_parse_valid = [number for number in column_to_parse \
if math.isnan(number) is False]
    valid_num = len(column_to_parse_valid)

    #If statement to test if valid numbers exist, if not, exit program.
    #If valid numbers exist, continue calculations.
    if valid_num == 0:
        sys.exit("Error: There were no valid number(s) in column {} in file: {}".\
format(sys.argv[2], sys.argv[1]))
    else:
        #calculate average of the list
        average_num = sum(column_to_parse_valid)/valid_num
        #calculate variance
        var_num = 0
        for i in range(valid_num):
            if valid_num == 1:
                var_num = 0
            else:
                var = ((column_to_parse_valid[i] - average_num)**2)/(valid_num-1)
                var_num = var_num + var
        #calculate standard deviation
        stdev_num = math.sqrt(var_num)
        #sort the item in list with increasing value, and then find the medium
        column_to_parse_valid.sort()
        #print(column_to_parse)
        if valid_num % 2 == 0:
            med_num = (column_to_parse_valid[int(valid_num/2-1)] + \
column_to_parse_valid[int(valid_num/2)])/2
        else:
            med_num = column_to_parse_valid[int((valid_num-1)/2)]

    print("column : {}\n\n".format(sys.argv[2]))
    print("Count\t\t=\t{:9.3f}".format(count_line))
    print("ValidNum\t=\t{:9.3f}".format(valid_num))
    print("Average\t\t=\t{:9.3f}".format(average_num))
    print("Maximum\t\t=\t{:9.3f}".format(max(column_to_parse_valid)))
    print("Minimum\t\t=\t{:9.3f}".format(min(column_to_parse_valid)))
    print("Variance\t=\t{:9.3f}".format(var_num))
    print("Std Dev\t\t=\t{:9.3f}".format(stdev_num))
    print("Median\t\t=\t{:9.3f}".format(med_num))

if __name__ == "__main__":
    main()
