# https://leetcode.com/problems/maximum-population-year/description/

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Create a population difference array for years 1950 to 2050
        year_range = 101  # From 1950 to 2050 inclusive
        pop_diff = [0] * year_range

        for birth, death in logs:
            pop_diff[birth - 1950] += 1
            pop_diff[death - 1950] -= 1  # death year is NOT included

        max_population = 0
        max_year = 1950
        curr_population = 0

        for i in range(year_range):
            curr_population += pop_diff[i]
            if curr_population > max_population:
                max_population = curr_population
                max_year = 1950 + i

        return max_year

        # Time - O(N + R)
        # SPace - O(R)

        