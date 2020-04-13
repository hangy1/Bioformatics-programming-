#!/usr/bin/env python3

#_UNIGENE_DIR = "ssh yin.hang1@defiance.neu.edu -t 'cd /data/PROGRAMMING/assignment5; bash --login'"
#ssh yin.hang1@defiance.neu.edu 'cd /data/PROGRAMMING/assignment5'

_UNIGENE_DIR = "./data_directories"
_UNIGENE_FILE_ENDING = "unigene"

def get_unigene_directory():
    return _UNIGENE_DIR

def get_uigene_extension():
    return _UNIGENE_FILE_ENDING

def get_host_keywords():
    bos_tarus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"
    host_keywords = {
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "mus_musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "ovis_aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus_norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus
    }
    return host_keywords

# Error" doesn't conform to snake_case naming style
# pylint: disable=C0103

def get_error_string_4_IOError(file, arg):  # error when used get_fh(file, "1234")
    """ Print the invalid argument type message and exits the program """
    print("Could not open the file: {} for type '{}'".format(file, arg))

def get_error_string_4_ValueError():  # error when used get_fh(file, "1234")
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Value for opening a file for reading/writing")

def get_error_string_4_TypeError():  # error when used get_fh(file, "r", "w")
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Type passed in:")

def get_error_string_4_PermissionError(file):
    """ Print the invalid argument type message and exits the program """
    print("Could not create the directory (permissions): {} ".format(file))

def get_error_string_4_FileNotFoundError(file):
    """ Print the invalid argument type message and exits the program """
    print("Could not create the directory (invalid argument): {} ".format(file))

def get_error_string_4_OSError(file):
    """ Print the invalid argument type message and exits the program """
    print("Could not create the directory (os error): {} ".format(file))

def get_error_string_4_unable_to_open(file):
    print("Could not open the directory (os error): {} ".format(file))
