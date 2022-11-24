def accum(string):
    simple_list = []
    for i in range(len(string)):
        simple_list.append(string[i] * int(str(i+1)))
    return "-".join(simple_list).title()
