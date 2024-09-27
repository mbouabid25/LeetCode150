""" Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
- Return k. """

class Solution(object):
    def removeElement(self, nums, val):
        # Use two pointers to modify the list in place
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        # Now the first 'i' elements are the modified list
        return i
    
    """ Example : nums = [0,1,2,2,3,0,4,2]
              val = 2
    First pass : 
    i = 0
    j = 0

    nums[j] = 0 is not equal to 2, so nums[i] = nums[j]. Since i = j, nothing changes. 
    i becomes 1. 

    Second pass : 
    i = 1
    j = 1

    nums[j] = 1 is not equal to 2, so nums[i] = nums[j]. Since i = j, nothing changes. 
    i becomes 2. 

    Third pass :
    i = 2
    j = 2 
    nums[j] = 2 is equal to 2. Nothing changes in the array. 

    Fourth pass : 
    i = 2
    j = 3

     nums[j] = 2 is equal to 2. Nothing changes in the array. 
    
    Fifth pass : 
    i = 2
    j = 4

    nums[j] = 3 is not equal to 2, so nums[i] = nums[j]. The array becomes nums = [0,1,3,2,3,0,4,2]
    i becomes 3

    Sixth pass : 
    i = 3
    j = 5

    nums[j] = 0 is not equal to 2, so nums[i] = nums[j]. The array becomes nums = [0,1,3,0,3,0,4,2]
    i becomes 4

    Seventh pass : 
    i = 4
    j = 6

    nums[j] = 4 is not equal to 2, so nums[i] = nums[j]. The array becomes nums = [0,1,3,0,4,0,4,2]
    i becomes 5

    nums[j] = 2 is equal to 2. Nothing changes in the array. 

    Final array : [0,1,3,0,4,0,4,2]


    Time complexity : 
    	1.	Single Loop Over the Array:
	•	The algorithm uses a for loop that iterates over the array nums from the first element to the last. This loop runs  n  times, where  n  is the number of elements in the array (len(nums)).
	•	In each iteration, the algorithm checks the current element (nums[j]) and decides whether to copy it to the front of the list (if it is not equal to val). This operation, including checking and copying, is a constant-time operation,  O(1) .
	2.	Operations Per Element:
	•	For each element, there are at most two operations: a comparison (nums[j] != val) and, if the comparison passes, a copy operation (nums[i] = nums[j]).
	•	Both of these operations are  O(1) , meaning their execution time does not depend on the size of the input but only on the individual element.
	3.	Overall Complexity:
	•	Since each element is visited once and handled in constant time, the total number of operations is proportional to the number of elements, i.e.,  O(n) . """