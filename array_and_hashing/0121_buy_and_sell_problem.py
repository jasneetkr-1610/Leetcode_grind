"""
PROBLEM STATEMENT:You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

DIFFICULTY LEVEL: Easy  

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""

def maxProfit(prices):
    l,r=0,1
    maxP=0

    while r<len(prices):
        if prices[r]>prices[l]:
            profit=prices[r]-prices[l]
            maxP=max(maxP,profit)

        else:
            l=r
        r+=1
    return maxP

prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5