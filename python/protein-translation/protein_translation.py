protein_dict = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
 }

def proteins(strand):
    protein_list = []
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for codon in codons:
        if codon in ('UAA', 'UAG', 'UGA'):
            break
        for cdn, protein in protein_dict.items():
            if cdn == codon:
                protein_list.append(protein)
    return protein_list
