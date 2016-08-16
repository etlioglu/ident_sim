"""
- read_msa : fasta to ordered dict
- compare : loop through ordered dict, do pairwise comparisons


Reads a multiple a sequence alignment file in FASTA/Pearson format and reports percent identity and percent similarity values of protein pairs.
Inspired by Ident and Sim (from Sequence Manipulation Suite) of bioinformatics.org.

Creates an ordered dictionary(OrderedDict) of fasta headers as indexes and sequences as values.
Word wrap sizes/line breaks do not matter while reading the (multi)fasta files.
Returns percent identity and percent similarity values.
"""

from __future__ import division
from collections import OrderedDict
import itertools

fasta_file = raw_input("Please enter the name of the fasta file: ")

def read_msa(file_name):

    seq_dict = OrderedDict()

    try:
        with open(file_name, "r") as seqfile:
            for line in seqfile:
                line = line.strip()
                if line[0] == ">":
                    seq_dict[line[1:]] = ""
                else:
                    seq_dict[next(reversed(seq_dict))] = seq_dict[next(reversed(seq_dict))] + line
    except:
        print fasta_file + " could not be found, exiting!"

    return seq_dict

def pairwise():
    seq_dict = read_msa(fasta_file)

    for pair in itertools.combinations(seq_dict.iteritems(), 2):
        compare(pair[0], pair[1])


def compare(tup1, tup2):

    iden = 0
    sim = 0
    head1 = tup1[0]
    seq1 = tup1[1]
    head2 = tup2[0]
    seq2 = tup2[1]
    align_len = 0
    min_len = min(len(seq1), len(seq2))

    for i in xrange(min_len):
        if seq1[i] == "-" and seq2[i] == "-":
            pass
        else:
            align_len += 1
            if seq1[i] == seq2[i]:
                iden += 1
                sim += 1
            elif seq1[i] in "GAVLI":
                if seq2[i] in "GAVLI":
                    sim += 1
            elif seq1[i] in "FYW":
                if seq2[i] in "FYW":
                    sim += 1
            elif seq1[i] in "CM":
                if seq2[i] in "CM":
                    sim += 1
            elif seq1[i] in "ST":
                if seq2[i] in "ST":
                    sim += 1
            elif seq1[i] in "KRH":
                if seq2[i] in "KRH":
                    sim += 1
            elif seq1[i] in "DENQ":
                if seq2[i] in "DENQ":
                    sim += 1
            elif seq1[i] in "P":
                if seq2[i] in "P":
                    sim += 1
            #else:
             #   return "Error! Check" + seq1[i] + " vs " + seq2[i]

    print head1 + " vs " + head2
    print "Alignment length: ", align_len
    print "Identical residues: ", iden
    print "Percent identity: ", round(iden / align_len * 100,2)
    print "Similar residues: ", sim-iden
    print "Percent similarity: " , round(sim / align_len * 100,2)
    print " "

pairwise()



