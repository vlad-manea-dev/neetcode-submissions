class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        seen = set(allowed)
        res = 0
        for s in words:
            working = 0
            for c in s:
                if c in seen:
                    working += 1
            if working == len(s):
                res += 1
        return res
                
        