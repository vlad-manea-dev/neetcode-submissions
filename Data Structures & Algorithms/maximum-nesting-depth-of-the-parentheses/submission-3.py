class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                res = max(res, len(stack) + 1)
                stack.append(c)
            elif c == ")":
                stack.pop()
        return res 

