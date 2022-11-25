def sum_two_smallest_numbers(numbers):
    first_digit = min(numbers)
    numbers.remove(min(numbers))
    two_digit = min(numbers)
    return first_digit + two_digit


#  another answer:
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])