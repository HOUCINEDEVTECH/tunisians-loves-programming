def get_max(numbers):
    max_val = numbers[0]
    for item in numbers:
        if item > max_val:
            max_val = item
    return max_val
