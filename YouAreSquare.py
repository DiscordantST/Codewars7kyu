def is_square(digit):
    if digit == 0:
        return True
    if digit < 0:
        return False
    else:
        return digit % digit ** 0.5 == 0
