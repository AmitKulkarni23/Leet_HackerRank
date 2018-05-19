# Program to find GCD of 2 numbers
# Inspired By: https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
def gcd(a, b):
    """
    Function to find gcd of 2 numbers a and b
    """
    if a == 0 or b == 0:
        print("No GCD")
        return None

    if a == b:
        return a

    if (a > b):
        return gcd(a - b, b)

    return gcd(a, b - a)

# Examples
print(gcd(12, 4))
print(gcd(18, 24))
