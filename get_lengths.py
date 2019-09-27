#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Sept 27 16:14 2019
@author: jasonbrant
"""

import os
import argparse

def read_fasta(fp):
    '''
    This function reads in FASTA file and returns a tuple containing the read ID and the sequence.
    :param fp:
    :return:
    '''
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

def get_lengths(dir_name, mode):
    if mode == 'alignment':
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
    if mode == 'ccs':
        for filename in os.listdir(dir_name):
            if filename.endswith("fa"):
                with open(filename) as fp:
                    outfile = open("MinMax_ReadLengths.txt", "w+")
                    lengths = os.path.splitext(filename)[0] + ".read_lengths.txt"
                    lengths = open(lengths, "w+")
                    read_length = []
                    for name, seq in read_fasta(fp):
                        if name.startswith(">"):
                            read_length.append(len(seq))
                            lengths.write("{}\t{}\n".format(name, (len(seq))))
                    max_length = max(read_length)
                    min_length = min(read_length)
                print("\n{}\nMax Read Length =\t{}\nMin Read Length =\t{}\n".format(filename, max_length, min_length))
                outfile.close()
                lengths.close()
    if mode == 'fasta':
        for filename in os.listdir(dir_name):
            ref_length = 0
            alignment_length = []
            if filename.endswith(".fa"):
                with open(filename) as fp:
                    first_read = True
                    for name, seq in read_fasta(fp):
                        if first_read:
                            ref_length = len(seq)
                            first_read = False
                        else:
                            alignment_length.append(len(seq))
                    diff = max(alignment_length) - min(alignment_length)
                    print("""Gene Name =\t{}
        Reference Length =\t{}
        Max Alignment Length =\t{}
        Min Alignment Length =\t{}
        Differene =\t{}

        """.format(filename, ref_length, max(alignment_length), min(alignment_length), diff))


parser = argparse.ArgumentParser(description = "Run get_fasta_lengths.py -h for help."
                                               "For 'alignment' and 'ccs' modes, this script will generate the "
                                               "lengths of aligned reads from an alignment fasta generated by bsDraw.py "
                                               "or the lengths of ccs reads. In 'fasta' mode, this will print to the "
                                               "screen the gene/fragment name, reference length, max alignment length, "
                                               "min alignment length and the difference between the "
                                               "max and min lengths. This is useful for trouble shooting or determining "
                                               "if filtering of alignments should be done. ")
parser.add_argument("dir_name", nargs = "?", default = os.getcwd(), help = "Directory containing the .fa files to be "
                                                                           "analyzed. ")
parser.add_argument('mode', help = "Mode to run in. Options are 'alignment', 'ccs', and 'fasta'. ")

if __name__ == "__main__":
    args = parser.parse_args()
    get_lengths(args.dir_name, args.mode)