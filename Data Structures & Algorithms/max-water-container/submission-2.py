class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # // 1. Brute Force
        #
        # n = len(heights)
        # aera = 0
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         loca = min(heights[i],heights[j]) * (j-i)
        #         aera = max(aera, loca)
        # return aera

        # 2. Two Pointers
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
