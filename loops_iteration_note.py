#!/usr/bin/env python3

#enumerate, the method that add the counter
for counter, number in enumerate([3,4,5,5,6], start=1):
    print(counter,number)

#Filter
number_list = [6,7,8,10,12]
filtered_list = list(filter(lambda x: 3 < x < 10, number_list))
print(filtered_list)

#using boolean variable
found = False
for number in [6,7,8,10,12]:
    if number == 10:
        found = True
        #break found = False
    print(found, number)
