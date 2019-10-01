# https://leetcode.com/discuss/interview-question/313719/

# You are on a flight and wanna watch two movies during this flight.
# You are given List<Integer> movieDurations which includes all the movie durations.
# You are also given the duration of the flight which is d in minutes.
# Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
#
# Find the pair of movies with the longest total duration and return they indexes.
# If multiple found, return the pair with the longest movie.
#
# Example 1:
#
# Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
# Output: [0, 6]
# Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)

# https://leetcode.com/discuss/interview-question/313719/
# Time -> O(n log n)
# Space -> O(n)

def flight_details(arr, k):
    # store the movies in a new list m
    # each entry in m is a tuple of (movie_duration, original_index)
    m = []
    for i in range(len(arr)):
        m.append((arr[i], i))

    # sort by durations
    m.sort(key=lambda x: x[0])

    k -= 30
    left = 0
    right = len(arr) - 1
    pairs = None
    global_minutes = 0

    while left < right:
        local_minutes = m[left][0] + m[right][0]
        if local_minutes <= k:
            if local_minutes == k :
                return [m[left][1], m[right][1]]
            elif local_minutes > global_minutes:
                global_minutes = local_minutes
                pairs = [m[left][1], m[right][1]]
            left += 1
        else:
            right -= 1
    return pairs

