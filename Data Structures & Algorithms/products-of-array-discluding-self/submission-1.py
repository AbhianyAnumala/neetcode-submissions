class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fact = 1
        zeroFact = 0
        for i in range(0,len(nums)):
            if (nums[i] == 0):
                zeroFact = zeroFact +1
            else:
                fact = fact * nums[i]
            print(i)

        print(fact)
        result = [0] * len(nums)

        if (zeroFact>1):
            return result
        elif(zeroFact == 1):
            for i in range(0,len(nums)):
                if  (nums[i]==0):
                    result[i] = fact
            return result
        else:
            for i in range(0,len(nums)):
                result[i] = int(fact/nums[i])
        return result 


        