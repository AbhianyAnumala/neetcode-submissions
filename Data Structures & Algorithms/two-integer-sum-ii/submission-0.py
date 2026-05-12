class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset = set(numbers)
        for i,num in enumerate(numbers):
            if (target - num in numset):
                return [i+1,numbers.index(target - num)+1]
        