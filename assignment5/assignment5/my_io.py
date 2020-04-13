'''
Here we have a a connection between submodules, i.e. my_io is using config
We have two options, we can use Absolute Module Imports or Explicit Relative Module Imports
'''

import os
from assignment5 import config


def is_valid_gene_file_name(file):
    if os.path.exists(file):
        return True
    else:
        return False

def get_fh(file, arg):
    try:
        fobj = open(file, arg)
        return fobj
    except IOError as err:
        config.get_error_string_4_IOError(file, arg)
        # raising like this  allows the overall application to choose whether
        # to stop running gracefully or handle the exception.
        # you could have a function you implment like log_the_error(err), and then raise
        raise err

    except ValueError as err:  # test something like my_io.get_fh("does_not_exist.txt", "rrr")
        config.get_error_string_4_ValueError()
        raise err

    except TypeError as err:  # test something like my_io.get_fh([], "r")
        config.get_error_string_4_TypeError()
        raise err

#def is_valid_gene_file_name(file):


def mkdir_from_infile(file):
    """
    void: mkdir_from_infile("/home/cleslin/test.txt")
    Takes : 1 argument, tries to create a directory from an infile string passed in
    Return : None
    """
    try:
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
    except PermissionError as err:
        config.get_error_string_4_PermissionError(file)
        # raising like this  allows the overall application to choose whether
        # to stop running gracefully or handle the exception.
        # you could have a function you implment like log_the_error(err), and then raise
        raise err
    except FileNotFoundError as err:
        # if the file is only a string with no /, you'll get : No such file or directory: ''
        config.get_error_string_4_FileNotFoundError(file)
        raise err
    except OSError as err:
        config.get_error_string_4_OSError(file)
        raise err







