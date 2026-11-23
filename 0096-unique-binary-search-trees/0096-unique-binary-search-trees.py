class Solution:
    def numTrees(self, n: int) -> int:
        count = [0] * (n + 1)
        count[0] = 1
        count[1] = 1
        for i in range(2, n + 1):              # i: number of nodes
            for r in range(1, i + 1):          # r: value at the root
                count[i] += count[r - 1] * count[i - r]
        return count[n]