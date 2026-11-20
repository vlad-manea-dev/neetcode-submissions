# 133

#1
# 32

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s = n*(n+1)//2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]