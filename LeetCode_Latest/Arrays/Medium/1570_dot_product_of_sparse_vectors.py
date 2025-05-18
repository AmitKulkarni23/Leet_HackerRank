# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

class SparseVector:
    """
    My Brute force which usese arrays
    """
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i in range(len(vec.vector)):
            result += self.vector[i] * vec.vector[i]
        
        return result

    """
    Time complexity: O(n) for both constructing the sparse vector and calculating the dot product.

    Space complexity: O(1) for constructing the sparse vector as we simply save a reference to the input array and O(1) for calculating the dot product.
    """
    

class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n              

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
    
    """
    Let n be the length of the input array and L be the number of non-zero elements.

    Time complexity: O(n) for creating the Hash Map; O(L) for calculating the dot product.

    Space complexity: O(L) for creating the Hash Map, as we only store elements that are non-zero. O(1) for calculating the dot product.
    """
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)