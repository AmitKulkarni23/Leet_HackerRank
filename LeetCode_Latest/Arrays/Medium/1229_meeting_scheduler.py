# https://leetcode.com/problems/meeting-scheduler/description/

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Time Complexity O(m log m + n log n)
        # Sort both slots by start time
        slots1.sort()
        slots2.sort()
        
        i, j = 0, 0
        
        while i < len(slots1) and j < len(slots2):
            # Find the overlap between slots1[i] and slots2[j]
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            
            # Check if overlap is enough for the meeting
            if end - start >= duration:
                return [start, start + duration]
            
            # Move the pointer that ends earlier
            # If the overlap is not large enough, we need to move forward in one of the lists to try to find a better overlap.
#             The overlap is bounded by the earlier end (min(slots1[i][1], slots2[j][1]))

# If you want a potentially larger or later overlap, you need to get rid of the interval that ends sooner, since it can't contribute to a bigger overlap going forward.
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        return []
