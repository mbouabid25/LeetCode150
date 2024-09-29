""" Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not. """

class Solution(object):
    def squareFct(self, n):  # Add 'self' to make it an instance method
        sum = 0
        for dig in str(n):
            sum += int(dig) * int(dig)
        return sum

    def isHappy(self, n):
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = self.squareFct(n)
        return n == 1

""" Explanation :
1 . squareFct(n): This helper function calculates the sum of the squares of the digits of the number n. For example, if n = 19, it computes 
1^2+9^2=82

2. isHappy(n): This function checks if n is a happy number:
It uses a set called seen to keep track of numbers that have been encountered during the process.
The while loop continues until n becomes 1 (indicating it's a happy number) or a repeated number is detected (indicating a cycle).
If n reaches 1, it returns True (meaning n is happy). If it detects a cycle (when n is in seen), it returns False. """

