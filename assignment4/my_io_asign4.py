 """
 2 Here we have a a connection between submodules, i.e. my_io is using config
 3 We have two options, we can use Absolute Module Imports or Explicit Relative Module Imports
 4 """
 5
 6 import os
 7
 8 # Absolute Module Import
 9 # Notice use of top-level package name (assignment 4)
10 from assignment4 import config
11
12 # Explicit Relative Module Imports
13 # Leading dots (.) used to move up hierarchy
14 # from .  import foo        Loads ./foo.py
15 # from .. import foo        Loads ../foo.py
16 # from ..grok import foo    Loads ../grok/foo.py
17
18 # from . import config
19
20 # Explicit Relative Module Imports: allow packages to be easily renamed
21 # here we rename spam to grok
22 # spam/                                  grok/
23 #     __init__.py                             __init__.py
24 #     foo.py              ----->              foo.py
25 #     bar.py                                  bar.py
26
27 # Explicit Relative Module Imports: Useful for moving code around, versioning, etc
28
29 # https://realpython.com/absolute-vs-relative-python-imports/
30
31
   def get_fh(file, arg):
33     """
34     filehandle : get_fh(infile, "r")
35     Takes : 2 arguments file name and mode i.e. what is needed to be done with
36     this file. This function opens the file based on the mode passed in
37     the argument and returns filehandle.
38     Returns : filehandle
39     """
40     try:
41         fobj = open(file, arg)
42         return fobj
43     except IOError as err:
44         config.get_error_string_4_IOError(file, arg)
45         # raising like this  allows the overall application to choose whether
46         # to stop running gracefully or handle the exception.
47         # you could have a function you implment like log_the_error(err), and then raise
48         raise err
49
50     except ValueError as err:  # test something like my_io.get_fh("does_not_exist.txt", "rrr")
51         config.get_error_string_4_ValueError()
52         raise err
53
54     except TypeError as err:  # test something like my_io.get_fh([], "r")
55         config.get_error_string_4_TypeError()
56         raise err
57
58
59 def mkdir_from_infile(file):
60     """
61     void: mkdir_from_infile("/home/cleslin/test.txt")
62     Takes : 1 argument, tries to create a directory from an infile string passed in
63     Return : None
64     """
65     try:
66         if not os.path.exists(os.path.dirname(file)):
67             os.makedirs(os.path.dirname(file))
68     except PermissionError as err:
69         config.get_error_string_4_PermissionError(file)
70         # raising like this  allows the overall application to choose whether
71         # to stop running gracefully or handle the exception.
72         # you could have a function you implment like log_the_error(err), and then raise
73         raise err
74     except FileNotFoundError as err:
75         # if the file is only a string with no /, you'll get : No such file or directory: ''
76         config.get_error_string_4_FileNotFoundError(file)
77         raise err
78     except OSError as err:
79         config.get_error_string_4_OSError(file)
80         raise err