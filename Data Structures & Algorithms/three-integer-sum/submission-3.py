class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # // 1. Brute Force O(n3), O(m)

        # n = len(nums)
        # res = set()
        # nums.sort()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if (nums[i]+nums[j]+nums[k] == 0):
        #                 ans = [nums[i],nums[j],nums[k]]
        #                 # ans.sort()
        #                 # if (ans not in res):
        #                 #     res.append(ans)
        #                 res.add(tuple(ans))
        # # return res
        # return [list(i) for i in res]

        # // 2. Two Pointers O(n2), O(m)
        n = len(nums)
        nums.sort()
        res = set()
        for i, a in enumerate(nums):
            l,r = i+1, n - 1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if  (threeSum > 0):
                    r-=1
                if (threeSum < 0):
                    l+=1
                if (threeSum == 0):
                    ans = [nums[i],nums[l],nums[r]]
                    l += 1
                    r -= 1
                    res.add(tuple(ans))
        return [list(i) for i in res]







