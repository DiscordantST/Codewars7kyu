def descending_order(num):
    simple_string = str(num)
    simple_list_c = []
    simple_list_b = []
    for i in range(len(simple_string)):
        simple_list_c.append(simple_string[i])
    simple_list_c.sort(reverse=True)
    for i in range(len(simple_list_c)):
        simple_list_b.append(simple_list_c[i])
    simple_list_b = "".join(simple_list_b)
    return int(simple_list_b)


print(descending_order(12345435))

