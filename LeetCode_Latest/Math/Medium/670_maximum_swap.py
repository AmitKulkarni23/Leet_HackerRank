# https://leetcode.com/problems/maximum-swap/description/

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits, as strings (e.g., 2736 -> ['2', '7', '3', '6'])
        digits = list(str(num))

        # Create a dictionary that tells us the last index (position) where each digit appears
        # For example, for 2736, it becomes: {2: 0, 7: 1, 3: 2, 6: 3}
        last = {int(d): i for i, d in enumerate(digits)}

        # Go through each digit from left to right
        for i, d in enumerate(digits):
            # Check for digits larger than the current digit (starting from 9 and going down)
            # We want to find if there's a bigger number we can swap with to the right
            for bigger in range(9, int(d), -1):
                # If that bigger digit exists and it comes after the current digit
                if last.get(bigger, -1) > i:
                    # We found a digit that is bigger and appears later in the number
                    # So, swap the current digit with the bigger one
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]

                    # Convert the list of digits back to a number and return it
                    return int(''.join(digits))

        # If we never found a swap that makes the number bigger, just return the original number
        return num








