def is_square(n):
    if n == 0:
        return True
    if n < 0:
        return False
    else:
        return n % n ** 0.5 == 0
