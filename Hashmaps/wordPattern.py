""" Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false """

class Solution(object):
    def wordPattern(self, pattern, s):
        hashmap = {}
        words = s.split()
        i = 0

        if len(pattern) != len(words):
            return False

        for char in pattern : 
            if char in hashmap:
                if hashmap[char] != words[i]:
                    return False
            else:
                if words[i] in hashmap.values():
                    return False
                hashmap[char] = words[i]
            i += 1
        return True
    

""" Explanation:
	1.	Initialization: The method initializes an empty dictionary hashmap to map characters from the pattern to 
    corresponding words from the string s. The string s is split into a list of words using the split() method, 
    and an index i is initialized to 0.
	2.	Length Check: It first checks if the lengths of pattern and words are the same. If they are not equal, 
    it immediately returns False because a pattern cannot match a different number of words.
	3.	Pattern Matching:
	•	The code iterates through each character in the pattern.
	•	If the character is already in the hashmap, it checks whether the associated word matches the current word at index i. 
    If not, it returns False.
	•	If the character is not in the hashmap, it checks if the current word is already mapped to a different character 
    (ensuring a one-to-one mapping). If it is, it returns False. Otherwise, it adds the character and word pair to the hashmap.
	4.	Index Increment: The index i is incremented after each iteration to move to the next word in the list.
	5.	Return: If the loop completes without returning False, the pattern matches the string, and the method returns True. """