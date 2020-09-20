def to_rna(dna_strand):
    rna_lookup = { 'G':'C', 'C':'G', 'T':'A', 'A':'U' }
    return ''.join([rna_lookup[n] for n in dna_strand])
    # return ''.join(map(rna_lookup.get, dna_strand))
