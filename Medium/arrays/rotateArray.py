""" Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100] """


class Solution(object):
    #Brute force
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        temp = []

        if k == 0:
            return None
        if len(nums) == 1 : 
            return None
        if k > len(nums):
            k = k % len(nums)
        for i in range(len(nums)-k,len(nums)):
            nums.append(nums[i])
        print("first version: " + str(nums))
        for i in range(len(nums)-k,k-1,-1):
            nums[i] = nums[i-k]
        print("second version: " + str(nums))
        for i in range(k):
            nums[i] = nums[i+len(nums)-k]
        print("third version: " + str(nums))
        for i in range(k):
            nums.pop()
        return None
    
""" Handling k larger than len(nums):
- correctly adjust k using k = k % len(nums) to handle cases where k is larger than the length of the array.
First loop (for i in range(len(nums)-k, len(nums))):
- append the last k elements of the array to the end of the nums array.
Second loop (for i in range(len(nums)-k, k-1, -1)):
- shift elements from earlier parts of the array to the correct positions.
Third loop (for i in range(k)):
- overwrite the first k elements with the last k elements from the end of the modified array.
Final loop (for i in range(k)):
- pop the last k elements from the nums array to restore the original length.

Time Complexity Analysis:
First loop: Appends k elements from the original array to the end, which takes O(k) time.
Second loop: Shifts elements of the array. Since it’s effectively going through up to n - k elements, it takes O(n - k) time.
Third loop: Overwrites the first k elements, which takes O(k) time.
Final loop: Pops k elements, which takes O(k) time.
In total, the time complexity is dominated by the sum of these operations: O(k)+O(n−k)+O(k)+O(k)=O(n)
Thus, the overall time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
Space for temp array: You’re using additional space by appending k elements to the array, which results in extra memory usage. 
This extra space usage is proportional to k.
Final space complexity: The space complexity is O(k) due to the temporary elements added to nums in the first loop. """
    
    #Optimized
def rotate(self, nums, k):
    def reverse(array, start,end):
            while start < end : 
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

            if k > len(nums):
                k = k%len(nums)
        
    reverse(nums, 0, len(nums)-1)

    reverse(nums, 0, k-1)
        
    reverse(nums, k, len(nums)-1)

    return None

    """ Explanation:
Handle k greater than the length of the array: By using k %= len(nums), we ensure that rotating by k 
steps is equivalent to rotating by k % len(nums) steps if k is larger than len(nums).
Reverse the entire array: This places the last k elements at the beginning, but in reverse order.
Reverse the first k elements: This puts the first k elements (the ones we want to rotate to the front) in the correct order.
Reverse the remaining elements: This restores the rest of the array (after the first k elements) to the correct order.

Time and Space Complexity:
Time complexity: O(n), where n is the length of the array. We perform three full reversals, each taking O(n).
Space complexity: O(1), since we modify the array in place and don’t use any extra space beyond a few variables.
This approach is more efficient than creating temporary arrays or using append and pop. """

