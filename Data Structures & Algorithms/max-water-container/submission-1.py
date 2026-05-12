class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        aera = 0
        for i in range(n-1):
            for j in range(i+1,n):
                loca = min(heights[i],heights[j]) * (j-i)
                aera = max(aera, loca)
        return aera
