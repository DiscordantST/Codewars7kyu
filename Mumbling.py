def accum(s):
    c = []
    for i in range(len(s)):
        c.append(s[i] * int(str(i+1)))
    return "-".join(c).title()




