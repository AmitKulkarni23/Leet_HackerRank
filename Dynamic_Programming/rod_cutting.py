# Given a rod of certain lenght and given prices of different lenghts selling in the
# market. How do you cut teh rod to maximize the profit?
###################################

def get_cut_rod_max_profit(arr, n):
    """
    Function that will return maximum profit that can be obtained by cutting
    teh rod into pieces and selling those pieces at market value

    L -> lenght of final rod
    arr -> array of prices

    Credits -> https://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/

    Time Complexity -> O(n ^ 2)
    """

    # Use dynamic programming
    # Create a 2D array

    cache = [0 for _ in range(n+1)]
    cache[0] = 0

    for i in range(1, n+1):
        max_val = float("-inf")
        for j in range(i):
            max_val = max(max_val, arr[j] + cache[i - j -1])

        cache[i] = max_val

    return cache[n]


# Examples
arr = [1, 5, 8, 9, 10, 17, 17, 20]
L = len(arr)
print(get_cut_rod_max_profit(arr, L))
