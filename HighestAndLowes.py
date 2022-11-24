def high_and_low(numbers):
    nums = [int(num) for num in numbers.split(' ')]
    return f"{max(nums)} {min(nums)}"
