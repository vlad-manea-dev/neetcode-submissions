class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        longest = 0
        sum_to_last_seen = {0: -1}
        for i,n in enumerate(nums):			
            if n == 0:
                sum -= 1
            elif n == 1:
                sum += 1
            if sum in sum_to_last_seen:
                longest = max(longest, i - sum_to_last_seen[sum])
            else:
                sum_to_last_seen[sum] = i  
        return longest
