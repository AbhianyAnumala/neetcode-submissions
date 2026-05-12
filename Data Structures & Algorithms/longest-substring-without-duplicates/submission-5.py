class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # maxl = 0
        # i = 0
        # while i < len(s):
        #     j = i + 1
        #     while j < len(s) and (ord(s[j]) - ord(s[j-1]) > 0):
        #         j+=1
        #     maxl = max(maxl,j-i) 
        #     i = j
        # return maxl

        # maxl = 0
        # i = 0
        # while i < len(s):
        #     j = i 
        #     du = set()
        #     while j < len(s) and s[j] not in du:
        #         du.add(s[j])
        #         j+=1
        #     maxl = max(maxl,len(du)) 
        #     i +=1
        # return maxl


        l,r = 0,0
        res = 0
        char = set()
        while r < len(s):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            res = max(res , r-l+1)
            r+=1
        return res
        