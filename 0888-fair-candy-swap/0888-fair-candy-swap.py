class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        diff = (sumB - sumA) // 2
        setB = set(bobSizes)
        
        for a in aliceSizes:
            if a + diff in setB:
                return [a, a + diff]