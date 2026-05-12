class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        days = len(prices)
        for i in range(days):
            buy = prices[i]
            for j in range(i+1,days):
                sell = prices[j]
                res = max(res, sell-buy)
        return res
            
