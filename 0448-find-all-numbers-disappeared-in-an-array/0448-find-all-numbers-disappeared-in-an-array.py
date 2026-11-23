class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        sudoku = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in sudoku:
                res.append(i)
        return res