def descending_order(num):
    a = str(num)
    c = []
    b = []
    for i in range(len(a)):
        c.append(a[i])
    c.sort(reverse=True)
    for i in range(len(c)):
        b.append(c[i])
    b = "".join(b)
    return int(b)

