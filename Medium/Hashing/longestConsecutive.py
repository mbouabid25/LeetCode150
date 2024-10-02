""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time. """

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indexes = set(nums)  # Store all numbers in a set for O(1) lookups
        max_count = 0

        for num in nums:
            # Only start counting if 'num' is the start of a sequence (i.e., num - 1 is not in the set)
            if num - 1 not in indexes:
                current = num
                count = 0

                # Count consecutive numbers starting from 'num'
                while current in indexes:
                    current += 1
                    count += 1
                
                # Update the maximum count found so far
                max_count = max(max_count, count)

        return max_count

solution = Solution()

""" Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
 """
print("Example 1, input:[100,4,200,1,3,2]")
print(solution.longestConsecutive([100,4,200,1,3,2]))

""" Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9 """

print("Example 2, input:[0,3,7,2,5,8,4,6,0,1]")
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

""" Problem Recap:
We are given an unsorted array of integers, and we need to find the length of the longest 
consecutive sequence. The solution must run in O(n) time complexity, where n is the number of elements in the array.

Explanation:
Using a Hash Set for Quick Lookups:
- We store all elements of the array in a hash set (indexes = set(nums)). The reason we use a set is because
it allows O(1) average-time lookups, which ensures that checking whether a number exists in the array is efficient.
Starting the Count Only at the Beginning of a Sequence:
- For each number num in the array, we check if it is the start of a sequence by verifying if num - 1 is not
 in the set. This ensures that we only count the sequence once, starting from the smallest number in that sequence.
For example, in the sequence [1, 2, 3, 4], the count will start at 1, but not at 2, 3, or 4, because their preceding numbers exist in the set, meaning they're part of an already counted sequence.
Counting the Length of the Sequence:
-Once we identify the start of a sequence (i.e., num - 1 is not in the set), we enter a while loop to count how many 
consecutive numbers exist by continuously checking num + 1, num + 2, etc., in the set.
-For each sequence, we calculate its length and update max_count if the current sequence is the longest one found so far.
Final Output:
After the loop completes, max_count will hold the length of the longest consecutive sequence, which we return. """

""" Time Complexity Analysis:

- Building the Set:
In the line indexes = set(nums), we are inserting all n elements from nums into the set. 
This operation takes O(n) time, where n is the number of elements in nums.
-Looping Through the Elements:
We loop through each element in nums exactly once in for num in nums:. The loop runs n times.
Inside the loop, we only start a new sequence when num - 1 is not in the set. 
This check is an O(1) operation because set lookups are constant time on average.
When we find the start of a sequence, we enter a while loop to count the length of the sequence. 
Since each element in the sequence is processed at most once, the total time spent in the while loops across all iterations of the for loop is also O(n). No element is counted more than once.
Thus, each element is processed at most twice: once in the for loop and once in 
the while loop (if it's the start of a sequence).
-Total Time Complexity:
The total time complexity is O(n) because:
1. Inserting elements into the set takes O(n).
2. The loop processes each element in O(n) total time, and each sequence is counted once.

Space Complexity:
The space complexity is O(n) because we are using a set to store all elements of the array, which requires 
space proportional to the number of elements (n). """