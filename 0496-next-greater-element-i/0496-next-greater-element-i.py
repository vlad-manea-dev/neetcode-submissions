class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        mapping = {}

        for n in nums2:
            while stack and n > stack[-1]:
                    mapping[stack.pop()] = n
            stack.append(n)
        
        for n in stack:
            mapping[n] = -1

        return [mapping[x] for x in nums1]
