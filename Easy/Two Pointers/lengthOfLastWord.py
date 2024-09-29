""" A word is a maximal substring
 consisting of non-space characters only.

 

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5. """



class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        last_word = words[len(words)-1]
        return len(last_word)
    

""" OR """

def lengthOfLastWord(self, s):
        i = len(s)-1
        count = 0

        if i == 0:
            return 1
        while(i >= 0 and s[i] == ' '):
            i-=1
        while( i >= 0 and s[i] != ' '):
            count += 1
            i -= 1
        return count