class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair index : temp

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                tempIndex, temp = stack.pop()
                res[tempIndex] = i - tempIndex
            stack.append((i, t))
        return res