""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]] """

class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        final = []

        for s in strs : 
            if ''.join(sorted(s)) in map:
                map[''.join(sorted(s))].append(s)
            else:
                map[''.join(sorted(s))] = [s]
        
        for value in map.values():
            final.append(value)

        return final
    
"""Explanation:

	1.	Sorting Each String: For each string s in strs, the string is sorted using sorted(s). The sorted string serves as the key for the dictionary.
	2.	Check and Group: If the sorted string exists as a key in the dictionary, append the original string to the list associated with that key. Otherwise, create a new entry with the sorted string as the key and the original string as the first element in the list.
	3.	Result: The values (lists of anagrams) are appended to the final list, which is returned.

Time Complexity:

	•	Sorting a string takes O(k log k), where k is the length of the string.
	•	Looping through all strings takes O(n), where n is the number of strings.
	•	Hence, the overall time complexity is O(n * k log k), where n is the number of strings, and k is the average length of each string.

Space Complexity:

	•	The dictionary stores all n strings, each of size k, so it uses O(n * k) space.
	•	The sorted version of each string takes additional space, contributing to the overall space complexity of O(n * k)."""

#OR

def groupAnagrams(self, strs):
        myDict = collections.defaultdict(list)
        
        for s in strs : 
            count = [0] * 26
            for c in s : 
                count[ord(c)-ord("a")] += 1
            myDict[tuple(count)].append(s)
        return myDict.values()

""" Explanation:

	1.	Character Frequency Count: Instead of sorting the string, this solution uses a frequency count of the characters. Each string is converted to a 26-element list where each index represents the count of a corresponding letter (from 'a' to 'z').
	2.	Use Frequency Count as Key: The frequency list is converted into a tuple (since tuples are hashable) and used as the key in the dictionary. All strings with the same character frequencies are grouped together.
	3.	Result: The values (lists of anagrams) from the dictionary are returned directly.

Time Complexity:

	•	Counting the frequency of characters takes O(k) for each string, where k is the length of the string.
	•	Looping through all strings takes O(n), where n is the number of strings.
	•	Hence, the overall time complexity is O(n * k), where n is the number of strings, and k is the average length of each string.

Space Complexity:

	•	The dictionary stores all n strings, each of size k, using O(n * k) space.
	•	Additionally, the character frequency tuple for each string also takes O(n) space (each tuple is of fixed size 26, independent of k).
	•	Hence, the overall space complexity is O(n * k). """
