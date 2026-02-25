# Problem: Best Time to Buy and Sell Stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Difficulty: Easy
# Topics: Array, Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) time | O(1) space
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit