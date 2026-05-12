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

        maxl = 0
        i = 0
        while i < len(s):
            j = i 
            du = set()
            while j < len(s) and s[j] not in du:
                du.add(s[j])
                j+=1
            maxl = max(maxl,len(du)) 
            i +=1
        return maxl
        