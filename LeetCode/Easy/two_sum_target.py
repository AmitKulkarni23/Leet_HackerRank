# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # My Solution: O(n^2)
        
        # Final list which will be appended with the
        # 2 required integers. This will be the list that will be returned
        # final_list = []
        
        # for i in range(len(nums) - 1):
            # for j in range(i+1, len(nums)):
                # if nums[i] + nums[j] == target:
                    # We have found 2 such integers
                    # final_list.append(i)
                    # final_list.append(j)
                    # break
        
        # return final_list
    
    
        # Proper way to do it one pass -> O(n)
		# This is because the look-up for a dictionary is O(1) in amortized cases
        # Create a dictionary of the form {num[i] : i}
        
        final_dict = {}
        
        # Iterate through the array
        for i in range(len(nums)):
            complement = target - nums[i]
            
            # If this complement is already present as a key in the
            # dictionary, then we are done
            if complement in final_dict.keys():
                return [final_dict[complement], i]
            
            # Else add this combination to the dictionary
            final_dict[nums[i]] = i