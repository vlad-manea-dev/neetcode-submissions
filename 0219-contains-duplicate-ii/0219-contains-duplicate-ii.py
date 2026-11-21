class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seenMap = {}

        for i,n in enumerate(nums):
            if n in seenMap and abs(seenMap[n] - i) <= k:
                return True
            else:
                seenMap[n] = i
        return False
