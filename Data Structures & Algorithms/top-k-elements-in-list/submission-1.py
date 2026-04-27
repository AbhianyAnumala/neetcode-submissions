class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        res = {}
        for i in nums:
            res[i] = res.get(i,0) + 1
        print (res)

        sorted_by_val = dict(sorted(res.items(), key=lambda item: item[1],reverse=True))
        print (sorted_by_val)
        ans =  list(sorted_by_val)[:k]
        return ans
        