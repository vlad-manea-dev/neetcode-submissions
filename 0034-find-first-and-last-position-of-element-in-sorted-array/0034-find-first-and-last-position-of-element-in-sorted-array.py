from bisect import bisect_right
from bisect import bisect_left

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l = bisect_left(nums, target)                 # l: first index with nums[l] >= target
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, bisect_right(nums, target) - 1]    # last index with nums[i] <= target

#    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def first(nums,target):
            l,r=0,len(nums)-1
            first=-1
            while l<=r:
                mid=l+(r-l)//2
                
                if nums[mid]==target:
                    first = mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return first
        def second(nums,target):
            l,r=0,len(nums)-1
            second=-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    second=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return second
        return [first(nums,target),second(nums,target)]