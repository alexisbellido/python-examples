import pprint
import json

def get_codon(path):
    codons = []
    with open(path) as file:
        # seq = file.read()
        # seq = seq.replace("\n", "")
        # seq = seq.replace("\r", "")
        for line in file:
            line = line.strip()
            # print(line.rstrip("\r\n"))
            parts = line.split(',')
            codon = {
                'codon': parts[0],
                'abv': parts[1],
                'code': parts[2],
                'name': parts[3],
            }
            codons.append(codon)
    return codons[1:]

if __name__ == '__main__':
    """
    Cells decode mRNAs by reading their nucleotides in groups of three,
    called codons.

    A codon is a sequence of three DNA or RNA nucleotides that corresponds with
    a specific amino acid or stop signal during protein synthesis. DNA and RNA
    molecules are written in a language of four nucleotides; meanwhile, the
    language of proteins includes 20 amino acids. Codons provide the key that
    allows these two languages to be translated into each other. Each codon
    corresponds to a single amino acid (or stop signal), and the full set of
    codons is called the genetic code. The genetic code includes 64 possible
    permutations, or combinations, of three-letter nucleotide sequences that
    can be made from the four nucleotides. Of the 64 codons, 61 represent amino
    acids, and three are stop signals. For example, the codon CAG represents
    the amino acid glutamine, and TAA is a stop codon. The genetic code is
    described as degenerate, or redundant, because a single amino acid may be
    coded for by more than one codon. When codons are read from the nucleotide
    sequence, they are read in succession and do not overlap with one another.

    The genetic code is degenerate. Some amino acids are encoded by more than
    one codon, inasmuch as there are 64 possible base triplets and only 20 amino acids.
    In fact, 61 of the 64 possible triplets specify particular amino acids and
    3 triplets (called stop codons) designate the termination of translation.
    Thus, for most amino acids, there is more than one code word.
    """

    codons = get_codon('codon_table.csv')
    # pprint.pprint(codons, indent=4)
    # dicitionary has to be valid json
    print(json.dumps(codons, indent=4, sort_keys=True))
