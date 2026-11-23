class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROWS, COLS = len(image), len(image[0])

        directions = (0, 1), (1, 0), (-1, 0), (0, -1)
        seen = set()

        def dfs(r,c, prevColour):
            if (min(r, c) < 0 or ROWS == r or c == COLS or (r,c) in seen 
                or  prevColour != image[r][c]):
                return
            seen.add((r,c))
            image[r][c] = color

            for dr, dc in directions:
                dfs(dr + r, dc + c, prevColour)
            
        dfs(sr,sc, image[sr][sc])
        return image