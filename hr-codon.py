import math
import os
import random
import re
import sys
from typing import Dict

start_codon: str = "AUG"
stop_codon: str = "STOP"
codon_to_amino_acid: Dict[str, str] = {
    "AUG": "Met",
    "CAA": "Gln",
    "CAG": "Gln",
    "GGU": "Gly",
    "GCG": "Ala",
    "UUU": "Phe",
    "UUC": "Phe",
    "UGG": "Trp",
    "UAA": stop_codon,
    "UAG": stop_codon,
    "UGA": stop_codon,
}

#
# Complete the functions below.
#

def protein_synthesis_part_one(dna):
    # Write your code here
        if len(dna) % 3 != 0:
            return 'INVALID'
        dna = dna.replace('T', 'U')
        proteins = []
        valid_codons = []
        start_index = 0
        found_stop = False
        for i in range(0, len(dna), 3):
            codon = dna[i:i + 3]
            if len(codon) == 3:
                if codon == start_codon:
                    start_index = i
        for i in range(start_index, len(dna), 3):
            codon = dna[i:i + 3]
            if len(codon) == 3:
                try:
                    if codon_to_amino_acid[codon] == stop_codon:
                        found_stop = True
                        break
                except KeyError:
                    return 'INVALID'
                try:
                    proteins.append(codon_to_amino_acid[codon])
                except KeyError:
                    return 'INVALID'
        if not found_stop:
            return 'INVALID'
        result = ' '.join(proteins)
        return result

def protein_synthesis_part_two(dna):
    # Write your code here
    exons = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]
        if codon.isupper():
            exons.append(codon)
    if len(exons) < 3:
        return 'INVALID'
    dna = ''.join(exons)
    return(protein_synthesis_part_one(dna))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # part = int(input().strip())
    #
    # dna = input()

    part = 1
    # dna = "CAA ATG CAG GCG TAA"
    # valid
    dna = "CAAATGCAGGCGTAA"

    # no stop codon
    # dna = "CAAATGCAGGCGCAA"

    # part = 2
    # dna = "uag ATG cag CAG uaa GCG uga TAA"
    # valid
    # dna = "uagATGcagCAGuaaGCGugaTAA"
    # dna = "ATG CAG GCG TAA"
    # dna = "ATGCAGGCGTAA"


    if part == 1:
        result = protein_synthesis_part_one(dna)
    else:
        result = protein_synthesis_part_two(dna)

    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()

    ####################
    # print(codon_to_amino_acid)
    # for key, value in codon_to_amino_acid.items():
    #     if key == start_codon:
    #         print('start', key, value)
    #     elif value == stop_codon:
    #         print('stop', key, value)
    #     else:
    #         print(key, value)
    #     # if a == stop_codon:
    #     #     print('stop')
    #     # print(key, value)
    #
    # print('--------')
    # print('start', start_codon)
    # print('stop', stop_codon)
