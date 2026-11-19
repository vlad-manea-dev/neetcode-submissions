class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        count = Counter(nums)                 # value -> how many times it appears
        points = [0] * (max(nums) + 1)        # points[x] = total for taking every x
        for value, c in count.items():
            points[value] = value * c

        rob1, rob2 = 0, 0                     # best total up to x-2, best up to x-1
        for p in points:
            rob1, rob2 = rob2, max(rob2, rob1 + p)
        return rob2