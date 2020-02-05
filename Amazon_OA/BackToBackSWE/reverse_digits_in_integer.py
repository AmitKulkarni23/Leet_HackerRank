# Reverse digits of an integer

# Input:
# 42 - 24
# -314 -> -413
# 0 -> 0

# Time: O(n) where n is the number of digits
# Space: O(1)

def reverse_integer(n):
    result = 0
    number = abs(n)

    while number:
        result *= 10
        result += number % 10
        number = number // 10

    return result if n >= 0 else -result

all_numbers = [1, -321, -413, 0, -6557, 9890]
for item in all_numbers:
    print(reverse_integer(item))
