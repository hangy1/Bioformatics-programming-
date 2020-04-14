#!/usr/bin/env python3

'''
submodule for get_gene_info.py
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
    except ValueError as err:
        config.get_error_string_4_ValueError()
        raise err
    except TypeError as err:
        config.get_error_string_4_TypeError()
        raise err
    except OSError as err:
        config.get_error_string_4_unable_to_open(file,arg)
        raise err












