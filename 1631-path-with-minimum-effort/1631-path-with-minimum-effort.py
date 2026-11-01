import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        N = len(heights)
        M = len(heights[0])
        minH = [(0,0,0)] # height, r, c
        heapq.heapify(minH)
        visit = set()
        while minH:
            cost, r, c = heapq.heappop(minH)
            if r == N - 1 and c == M - 1:
                return cost
            if (r,c) in visit:
                continue
            visit.add((r, c))
            for dr, dc in directions:
                neir, neic = dr + r, dc + c
                if min(neir, neic) < 0 or neir == N or neic == M or (neir,neic) in visit:
                    continue
                new_cost = max(cost, abs(heights[r][c] - heights[neir][neic]))
                heapq.heappush(minH, (new_cost, neir, neic))
            
