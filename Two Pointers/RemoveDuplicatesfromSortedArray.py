""" Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each 
unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present 
in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k. """


class Solution:
    def removeDuplicates(self, nums):
        if not nums:  # Check if the list is empty
            return 0
        
        i = 0  # Pointer for the last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1  # Move the pointer i to the next position
                nums[i] = nums[j]  # Update nums[i] with the new unique element
        
        return i + 1  # Return the number of unique elements
    

""" Walkthrough:

Let’s apply this solution to the array nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]:

	1.	Initial State:
	•	nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	•	i = 0 (pointing at the first element)
	2.	Iteration:
	•	j = 1: nums[1] = 0, same as nums[0], so no change.
	•	j = 2: nums[2] = 1, different from nums[0], so increment i to 1 and update nums[1] to 1.
New nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4].
	•	j = 3: nums[3] = 1, same as nums[1], so no change.
	•	j = 4: nums[4] = 1, same as nums[1], so no change.
	•	j = 5: nums[5] = 2, different from nums[1], so increment i to 2 and update nums[2] to 2.
New nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4].
	•	j = 6: nums[6] = 2, same as nums[2], so no change.
	•	j = 7: nums[7] = 3, different from nums[2], so increment i to 3 and update nums[3] to 3.
New nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4].
	•	j = 8: nums[8] = 3, same as nums[3], so no change.
	•	j = 9: nums[9] = 4, different from nums[3], so increment i to 4 and update nums[4] to 4.
New nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4].
	3.	Final State:
	•	i = 4, so k = i + 1 = 5.
	•	The first k elements of nums are [0, 1, 2, 3, 4], the unique elements.

Time Complexity:

	•	The time complexity is  O(n)  because we iterate through the array once.

Space Complexity:

	•	The space complexity is  O(1)  since we are modifying the array in place without using extra space for another array.
    
 """