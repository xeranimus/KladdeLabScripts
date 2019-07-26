#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 10 13:06:34 2019

@author: jasonbrant
"""

import os
import argparse


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        line = line.replace("-", "")
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))

def get_lengths(dir_name):
    for filename in os.listdir(dir_name):
        if filename.endswith("fa"):
            with open(filename) as fp:
                outfile = open("MinMax_ReadLengths.txt", "w+")
                lengths = os.path.splitext(filename)[0] + ".read_lengths.txt"
                lengths = open(lengths, "w+")
                first_read = True
                read_length = []
                for name, seq in read_fasta(fp):
                    if first_read:
                        first_read = False
                        continue
                    if name.startswith(">"):
                        read_length.append(len(seq))
                        lengths.write("{}\t{}\n".format(name, (len(seq))))
                max_length = max(read_length)
                min_length = min(read_length)
            print("\n{}\nMax Read Length =\t{}\nMin Read Length =\t{}\n".format(filename, max_length, min_length))
            outfile.close()
            lengths.close()

parser = argparse.ArgumentParser(description = "Run get_alignment_lengths.py -h for help."
                                               "Run this script in the output directory of bsDraw to generate the "
                                               "lengths of aligned reads from an alignment fasta generated by bsDraw.py. "
                                               "This will read all the .fa files in the output directory of bsDraw and "
                                               "return a file with the minimum and maximum alignment lengths for each "
                                               "(This will also print to the screen). It will also generate a file for "
                                               "each that has each read ID and the alignment length. ")
parser.add_argument("dir_name", nargs = "?", default = os.getcwd(), help = "Directory containing the .fa files to be "
                                                                           "analyzed. ")

if __name__ == "__main__":
    args = parser.parse_args()
    get_lengths(args.dir_name)