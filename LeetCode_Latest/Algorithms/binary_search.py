def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Why do we need to do this for calculating mid - https://thebittheories.com/the-curious-case-of-binary-search-the-famous-bug-that-remained-undetected-for-20-years-973e89fc212
        # Why low <= high - we don't want to miss case wher ethe search space only contains one element
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

print(binary_search([1, 2, 3, 4, 5, 6], 55))
