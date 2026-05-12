class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0 
        # days = len(prices)
        # for i in range(days):
        #     buy = prices[i]
        #     for j in range(i+1,days):
        #         sell = prices[j]
        #         res = max(res, sell-buy)
        # return res

        l,r = 0,1
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r +=1
        return maxp
            
