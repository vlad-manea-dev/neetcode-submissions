class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        

        def backtrack(i, total, cur):
            if len(cur) == k and total == n:
                res.append(cur.copy())
                return
            if len(cur) > k or total > n or i > 8:
                return
            
            cur.append(i + 1)
            backtrack(i + 1, total + i + 1, cur)
            cur.pop()
            backtrack(i + 1, total, cur)

                
        backtrack(0,0, [])
        return res
