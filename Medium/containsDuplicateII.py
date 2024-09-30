""" Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false """

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        indexes = {}

        for i in range(len(nums)) : 
            if nums[i] in indexes : 
                if abs(i-indexes[nums[i]]) <= k:
                    return True
            indexes[nums[i]] = i
        return False


""" Steps:
Initialize an empty hash map (dictionary) to keep track of the last seen index of each element.
Iterate through the array:
For each element nums[i], check if it has been seen before (i.e., it's in the hash map).
If the element has been seen before, check if the difference between the current index and 
the last seen index is less than or equal to 𝑘
If the condition is satisfied, return true.
Otherwise, update the hash map to store the current index as the last seen index of this element.
If no such pair is found by the end of the iteration, return false. """