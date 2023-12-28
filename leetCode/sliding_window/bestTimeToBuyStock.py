"""
Question:
    121. Best time to buy and sell stock

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        while(j < len(prices)):
            if(prices[j] <= prices[i]):
                i,j = j, j+1
            elif(prices[j] > prices[i]):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
                j += 1
            
        return max_profit

solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4]))

"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
    1. Brute force = O(n^2)
"""