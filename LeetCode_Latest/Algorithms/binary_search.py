def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    found = False

    while low <= high and not found:
        # Why do we need to do this for calculating mid - https://thebittheories.com/the-curious-case-of-binary-search-the-famous-bug-that-remained-undetected-for-20-years-973e89fc212
        mid = low + (high - low) // 2
        if arr[mid] == target:
            found = True
        
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return found

print(binary_search([1, 2, 3, 4, 5, 6], 55))
