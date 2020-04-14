#!/usr/bin/env python3
"""
submodule of my_io.py and get_gene_info.py
"""

_UNIGENE_DIR = "./data_directories"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    """
    file directory path
    :return:
    """
    return _UNIGENE_DIR


def get_uigene_extension():
    """
    file suffix
    :return:
    """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
    create a dictionary for mapping common names to scientific names
    :return:
    """
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


def get_error_string_4_unable_to_open(file, arg):
    """ Print the invalid argument type message and exits the program """
    print("Could not open the file: {} for type '{}'".format(file, arg))


def get_error_string_4_ValueError():  # error when used get_fh(file, "1234")
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Value for opening a file for reading/writing")


def get_error_string_4_TypeError():  # error when used get_fh(file, "r", "w")
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Type")




