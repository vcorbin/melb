from Nucleotide import *
dna = NucleotideSequence("ACGACC")

assert dna.sequence == "ACGACC"

assert dna.base_count("A") == 2
assert dna.base_count("C") == 3
assert dna.base_count("T") == 0

assert dna.base_counts =={"A":2,"C":3,"T":0}

assert dna.gc_content() == 4.0/6.0

dna = NucleotideSequence("AAT")
assert dna.gc_content() == 0

dna = NucleotideSequence("CCGGGC")
assert dna.gc_content() == 1

dna = NucleotideSequence("AATCGC")
assert dna.reverse_complement() == "GCGATT"
dna = NucleotideSequence("")
assert dna.reverse_complement() == ""
