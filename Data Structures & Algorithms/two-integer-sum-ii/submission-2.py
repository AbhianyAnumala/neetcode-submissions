class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numset = set(numbers)
        # for i,num in enumerate(numbers):
        #     if (target - num in numset):
        #         return [i+1,numbers.index(target - num)+1]
        
        # i,j = 0, len(numbers)-1
        # while i<j:
        #     if (numbers[i]+numbers[j]== target):
        #         return [i+1,j+1]
        #     if (numbers[i]+numbers[j] > target):
        #             j-=1
        #     if (numbers[i]+numbers[j] < target):
        #             i+=1   
        # return [i+1,j+1]

        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return [i+1,j+1]
