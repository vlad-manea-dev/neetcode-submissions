class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        res = ""
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            if n == "0" and len(stack) == 0:
                continue
            stack.append(n)
        
        while k != 0 and stack:
            stack.pop()
            k -= 1
        res = "".join(stack)

        return res if len(res) > 0 else "0"
