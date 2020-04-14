chr21_gene_names.py
Overview:
This program takes one argument, asks the user to enter a gene symbol(case insensitive) and then \
prints the description for that gene based on data from the chr21_genes.txt file.
Example: python3 chr21_gene_names.py -i chr21_genes.txt
Test files: chr21_genes.txt

categories.py
Overview:
This program takes two arguments, counts genes occurrence in each category (1.1, 1.2, 2.1 etc.) \
based on data from the chr21_genes.txt file, then match it with its description file:chr21_genes_categories.txt
The output file is located at: OUTPUT/categories.txt
Example: python3 categories.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
Test files: chr21_genes.txt chr21_genes_categories.txt

intersection.py
Overview:
This program takes two argument, finds all gene symbols that appear both in two files. \
These gene symbols are printed to a file in alphabetical order with path OUTPUT/intersection_output.txt
Example: python3 intersection.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
         python3 intersection.py -i1 hgnc_complete_set_reduced.txt -i2 HUGO_genes.txt
         python3 intersection.py -i1 gene_age.txt -i2 chr21_genes.txt
Test files: chr21_genes.txt, HUGO_genes.txt; hgnc_complete_set_reduced.txt, \
            HUGO_genes.txt; gene_age.txt, chr21_genes.txt

