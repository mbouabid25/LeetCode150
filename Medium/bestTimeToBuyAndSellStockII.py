class Solution(object):
    def maxProfit(self, prices):
        '''What I need to do : find the highest and lowest values in the list, 
        in order. Calculate the profit'''

        i = 1
        profit = 0

        while i < len(prices):
            if prices[i] > prices[i-1]:
                profit += (prices[i]-prices[i-1])
            i += 1
        return profit
    
    """ Explanation : 
    - We can think of this approach as a greedy algorithm. Here’s a step-by-step breakdown of what you need to do:
    - Initialize a variable profit to 0. This will hold the total profit you make.
    - Loop through the prices array, starting from the second day (index 1).
    - For each day i, check if the price on day i is greater than the price on day i-1.
    - If it is, add the difference (prices[i] - prices[i-1]) to the profit.
    - Continue this process for the entire array. """