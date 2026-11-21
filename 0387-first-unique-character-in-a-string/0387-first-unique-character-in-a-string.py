class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for char, charCount in count.items():
            if charCount == 1:
                return s.index(char)
        return -1