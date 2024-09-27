""" Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. """

class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        count = 0

        for i in range(len(s)):
            count += roman[s[i]]
            print(count)
            if i >= 1 and roman[s[i-1]] < roman[s[i]]:
                count -= 2 * roman[s[i-1]]
        return count
    
"""     Explanation of the Code:

	1.	Dictionary Setup:
	•	A dictionary called roman is created to map Roman numeral characters ('I', 'V', 'X', 'L', 'C', 'D', 'M') to their respective integer values.
	2.	Initialization:
	•	A variable count is initialized to 0 to keep track of the total integer value of the Roman numeral string s.
	3.	Loop through the String:
	•	The code iterates through each character in the string s using a for loop and an index i.
	4.	Add the Value:
	•	For each character, its corresponding value from the roman dictionary is added to count.
	5.	Check for Subtraction Cases:
	•	If the current character represents a larger value than the previous character (e.g., 'IV'), it indicates a subtraction case.
	•	The code checks if i >= 1 (to ensure there is a previous character) and if the previous character’s value is less than the current one.
	•	If the condition is met, it subtracts twice the value of the previous character (2 * roman[s[i-1]]) to correct the total, as the previous addition was counted as positive.
	6.	Return the Result:
	•	After the loop completes, the final value of count is returned, representing the integer value of the Roman numeral string.

Example Walkthrough:

For the input "IX":

	•	I adds 1 (count = 1).
	•	X adds 10 (count = 11).
	•	Since I comes before X and I < X, 2 * 1 is subtracted (count = 9). """
        

