Assignment5 Overview:
get_gene_info.py module take two arguments: Host and Gene to extract gene expressed tissue
list.config.py and my_io.py are submodules of get_gene_info.py. Test scripts are located at tests
directory.

Example:
python3 get_gene_info.py
python3 get_gene_info.py -host "Homo sapiens" -gene AATK

pytest:
pytest --cov-report html --cov --cov-config=.coveragerc