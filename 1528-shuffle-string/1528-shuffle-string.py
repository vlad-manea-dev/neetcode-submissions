class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        a = list(s)
        for i in range(len(s)):
            a[indices[i]] = s[i]
        return "".join(a)