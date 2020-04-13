"""
 2 This Module is used for configuration, first its starts with error printing
 3 """
 4
 5 # Error" doesn't conform to snake_case naming style
 6 # pylint: disable=C0103
 7
 8
 9 def get_error_string_4_IOError(file, arg):  # error when used get_fh(file, "1234")
10     """ Print the invalid argument type message and exits the program """
11     print("Could not open the file: {} for type '{}'".format(file, arg))
12
13
14 def get_error_string_4_ValueError():  # error when used get_fh(file, "1234")
15     """ Print the invalid argument type message and exits the program """
16     print("Invalid argument Value for opening a file for reading/writing")
17
18
19 def get_error_string_4_TypeError():  # error when used get_fh(file, "r", "w")
20     """ Print the invalid argument type message and exits the program """
21     print("Invalid argument Type passed in:")
22
23
24 def get_error_string_4_PermissionError(file):
25     """ Print the invalid argument type message and exits the program """
26     print("Could not create the directory (permissions): {} ".format(file))
27
28
29 def get_error_string_4_FileNotFoundError(file):
30     """ Print the invalid argument type message and exits the program """
31     print("Could not create the directory (invalid argument): {} ".format(file))
32
33
34 def get_error_string_4_OSError(file):
35     """ Print the invalid argument type message and exits the program """
36     print("Could not create the directory (os error): {} ".format(file))