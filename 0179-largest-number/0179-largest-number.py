class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        arr = [str(n) for n in nums]

        from functools import cmp_to_key

        def cmp(a, b):
            ab = a + b
            ba = b + a
            if ab > ba:
                return -1
            if ab < ba:
                return 1
            return 0
        arr.sort(key=cmp_to_key(cmp))
        if arr[0] == "0":
            return "0"
        return "".join(arr)