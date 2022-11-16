def square_digits(num):
    simpleDigits = ''.join(str(int(i) ** 2) for i in str(num))
    return int(simpleDigits)