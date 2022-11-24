def DNA_strand(dna):
    c = []
    for i in dna:
        if i == "A":
            c.append("T")
        if i == "T":
            c.append("A")
        if i == "C":
            c.append("G")
        if i == "G":
            c.append("C")
    return "".join(c)

#  good answer
#  Azuaron, yannche, MolloOXx, D0425434, rxsilva, dprez808, pklecha, Holly Olly Oxen Free, AcostaDavid, DrMoriarty74 (+ 48)
#def DNA_strand(dna):
#return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])

