""" You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array 
represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise. """



class Solution(object):
    def canJump(self, nums):
        max_index = 0 

        for i in range(len(nums)):
            if i > max_index: 
                return False
            max_index = max(max_index, i + nums[i])
            
            if max_index > len(nums)-1:
                return True
        
""" Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
 """
solution = Solution()
print("Example 1, Input: nums = [2,3,1,1,4]")
print(solution.canJump([2,3,1,1,4]))

""" Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index. """

print("Example 2, Input: nums = [3,2,1,0,4]")
print(solution.canJump([3,2,1,0,4]))

        
        