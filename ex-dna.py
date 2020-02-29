import math


def get_sequence(path):
    with open(path) as file:
        seq = file.read()
        seq = seq.replace("\n", "")
        seq = seq.replace("\r", "")
        # for line in file:
        #     print(line.rstrip("\r\n"))
    return seq

def translate(seq):
    """
    In translation, the sequence of nucleotides in the mRNA is translated
    into a sequence of amino acids in a polypeptide (protein chain).
    """

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        if len(codon) == 3:
            protein += table[codon]

    return protein

if __name__ == '__main__':
    """
    We can think of DNA as a one dimensional string of characters with
    four characters to choose from. These characters are A, C, G, and T.

    They stand for the first letters with the four nucleotides used to
    construct DNA. The full names of these nucleotides are Adenine, Cytosine,
    Guanine, and Thymine.

    Each unique three-character sequence of nucleotides, sometimes called a
    nucleotide triplet, corresponds to one amino acid.

    The sequence of amino acids is unique for each type of protein and all
    proteins are built from the same set of just 20 amino acids for all
    living things.
    """

    dna = get_sequence('dna-original.txt')
    print('sequence')
    print('=================')

    # protein = translate(dna)
    protein = translate(dna[20:935])
    print('processed protein')
    print(protein)
    print('=================')

    original_protein = get_sequence('protein-original.txt')
    print('original protein')
    print(original_protein)
    print('=================')

    print('proteins match', protein == original_protein)

    # combination with repetition of n things in groups of r
    # https://www.mathsisfun.com/combinatorics/combinations-permutations.html
    # n = 4
    # r = 3
    # combinations = int(math.factorial(r + n -1) / (math.factorial(r) * math.factorial(n - 1)))
    # print(f'combinations with repetition of {n} things in groups of {r}: {combinations}')
