# https://leetcode.com/problems/reorder-data-in-log-files/
#
# Time Complexity – O(N log N) - sorting
# Space Complexity – O(N); we are using additional lists
# Custom sort.
# Using multiple keys to sort

# ----------------------------------


def reorderLogFiles(logs):
    # Credits -> https://leetcode.com/problems/reorder-data-in-log-files/discuss/198197/simple-Python3-solution-beats-99
    # Credits -> https://leetcode.com/problems/reorder-data-in-log-files/solution/
    # Time Complexity : O(N log N) where N is the number of log records
    # Space Complexity: O(N)

    digit_logs, letter_logs = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    # Sorting by multiple keys
    letter_logs.sort(key=lambda l: (l.split()[1:], l.split()[0]))
    return letter_logs + digit_logs

#         def custom_sort_func(log):
#             log_id, rest = log.split(" ", 1)

#             return (0, rest, log_id) if rest[0].isalpha() else (1, 0)

#         return sorted(logs, key=custom_sort_func)

