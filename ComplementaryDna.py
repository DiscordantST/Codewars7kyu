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

# good answer
# def DNA_strand(dna): return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])

