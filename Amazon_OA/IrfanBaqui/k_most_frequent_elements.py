# Given an input array of integers return the k most frequent elements
# Eg: Input: [1, 6, 2, 1, 6, 1, 6]
# Output: [1, 6]

# Time: O(n)
# Space: O(n)


def freqK(arr, k):
    freq = {}
    bucket = [None] * (len(arr) + 1)

    # Form the frequency map
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Iterate through the frequency map and populate the bucket array
    for key in freq:
        f = freq[key]

        if bucket[f] is None:
            bucket[f] = [key]
        else:
            bucket[f].append(key)

    # print(freq)
    # print(bucket)
    results = []
    for i in range(len(bucket) - 1, -1, -1):
        if bucket[i]:
            for item in bucket[i]:
                results.append(item)
                if len(results) >= k:
                    return results

    return results

input = [1, 6, 2, 1, 6, 1, 6, 4, 2]
k = 3

print(freqK(input, k))
