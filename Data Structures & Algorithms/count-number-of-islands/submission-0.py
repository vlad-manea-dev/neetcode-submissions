from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])

        def explore(r: int, c: int) -> bool:
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            
            if grid[r][c] == '0':
                return False
            
            pos = (r, c)
            if pos in visited:
                return False
            visited.add(pos)
            
            explore(r - 1, c)
            explore(r + 1, c)
            explore(r, c - 1)
            explore(r, c + 1)
            
            return True

        for r in range(rows):
            for c in range(cols):
                if explore(r, c):
                    count += 1

        return count