""" Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the" """


class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        new = ''
        i = len(words) - 1

        while i > 0:
            new += words[i] + " "
            i -= 1
        if i == 0:
            new += words[i]
        return new
    
# OR 

    def reverseWords(self, s):
        # Split the string into words, reverse the list of words, and join them with spaces
        return ' '.join(s.split()[::-1])