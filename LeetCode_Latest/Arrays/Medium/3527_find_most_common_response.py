# https://leetcode.com/problems/find-the-most-common-response/description/

class Solution:
    def findCommonResponse(self, responses) -> str:
        # Time Complexity - Time Complexity: O(N * M) where N = number of days, M = average number of responses per day.

        # Space Complexity: O(R) where R = total number of unique responses across all days.
        responses_non_duplicate_list = [[] for _ in range(len(responses))]

        for idx, response in enumerate(responses):
            seen = set()
            for item in response:
                if item not in seen:
                    seen.add(item)
                    responses_non_duplicate_list[idx].append(item)
            
        max_count_dict = {}
        for response in responses_non_duplicate_list:
            for item in response:
                max_count_dict[item] = max_count_dict.get(item, 0) + 1

        max_freq = max(max_count_dict.values())
        most_common = [k for k, v in max_count_dict.items() if v == max_freq]

        # The min operation in Python works and returns the lexicographically smallest
        return min(most_common)                    


