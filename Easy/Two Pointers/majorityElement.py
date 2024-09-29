""" Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Solve the problem in linear time and in O(1) space. """

class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count +=1
            else:
                count -=1
        return candidate
    
""" Why this works :
Count Balancing (Boyer-Moore Voting Algorithm): The algorithm maintains a balance between the candidate and other elements. 
When the count is zero, it effectively "resets" the candidate. 
This means that if an element is truly the majority, it will ultimately outweigh all other elements. """

