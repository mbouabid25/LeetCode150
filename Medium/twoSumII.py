""" Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2]. """




class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i + 1, j + 1]
            elif current_sum > target:
                j -= 1
            else:
                i += 1

""" Solution Explanation:

The problem asks us to find two numbers in a sorted array whose sum equals a given target. We can solve this efficiently using the two-pointer technique:

	1.	Two Pointers:
	•	Start with one pointer (i) at the beginning of the array and another pointer (j) at the end.
	•	Calculate the sum of the elements at these two pointers (numbers[i] + numbers[j]).
	2.	Adjust the Pointers:
	•	If the sum is equal to the target, return the 1-based indices [i+1, j+1].
	•	If the sum is greater than the target, move the j pointer left (decrement j) to try to reduce the sum.
	•	If the sum is less than the target, move the i pointer right (increment i) to increase the sum.
	3.	Repeat: Continue adjusting the pointers until the correct pair is found.

Time Complexity Analysis:

	•	Time Complexity: O(n), where n is the length of the input array.
	•	In each iteration of the loop, either the left pointer i moves right or the right pointer j moves left. Since each pointer only moves a maximum of n times (once per iteration), the loop runs at most n times, giving an overall time complexity of O(n).

Space Complexity Analysis:

	•	Space Complexity: O(1) because we are only using a fixed number of variables (i, j, current_sum), regardless of the size of the input array. No additional data structures are used. """
    
