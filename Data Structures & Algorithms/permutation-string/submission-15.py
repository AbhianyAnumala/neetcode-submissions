class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)>len(s2)): 
            return False
        if(len(s1)== 1): 
            if s1 in s2: 
                return True 
            else:
                return False
        
        count1 = {}
        for i in s1:
            count1[i] = count1.get(i,0) + 1

        need = len(count1)

        for l in range(len(s2)):
            if  s2[l] in count1:
                r = l
                ld = {}
                curr = 0
                while r < len(s2):
                    # print(ld)
                    ld[s2[r]] = ld.get(s2[r],0) + 1
                    if ld[s2[r]] > count1.get(s2[r],0):
                        break
                    if ld[s2[r]] == count1.get(s2[r],0):
                        curr+=1
                    if curr == need:
                        return True
                    r+=1
        return False   

        # for l in range(len(s2)):
        #     if  s2[l] in s1:
        #         r = l + len(s1)
        #         for i in range(l,r):
        #             if s2[i] not in s1:

        #         if r-l == len(s1):
        #              return True
        # return False   
                

        