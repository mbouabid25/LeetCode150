""" Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of 
the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not). """

class Solution(object):
    def isSubsequence(self, s, t):
        j = 0  # Pointer for string t

        # Iterate over each character in s
        for char in s:
            # Move the pointer j until we find a match or run out of characters in t
            while j < len(t) and t[j] != char:
                j += 1
            
            # If we've reached the end of t and haven't found the character, it's not a subsequence
            if j == len(t):
                return False

            j += 1
        
        return True
    
""" Detailed Example:

Consider s = "ace" and t = "abcde":

	•	Iteration 1:
	•	char = 'a' from s
	•	t[j] = 'a' (match found)
	•	j increments to 1 for the next comparison
	•	Iteration 2:
	•	char = 'c' from s
	•	t[j] = 'b' (no match, increment j)
	•	t[j] = 'c' (match found)
	•	j increments to 3 for the next comparison
	•	Iteration 3:
	•	char = 'e' from s
	•	t[j] = 'd' (no match, increment j)
	•	t[j] = 'e' (match found)
	•	j increments to 5

At the end of this process, all characters of s have been matched in order within t, confirming that s is a subsequence of t.
 """
            