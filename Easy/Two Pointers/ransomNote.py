""" Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote. """

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}
        for char in magazine:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for letter in ransomNote:
            if letter in count and count[letter] > 0:
                count[letter] -= 1  # Use one occurrence of the letter
            else:
                return False  # If the letter is not available or used up
        
        return True
    
    

