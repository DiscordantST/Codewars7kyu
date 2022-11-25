def get_sum(a, b):
    sum_digit = 0
    if a == b:
        print(a)
    if b < a:
        a, b = b, a
    for i in range(a, b + 1):
        sum_digit += i
    return sum_digit
