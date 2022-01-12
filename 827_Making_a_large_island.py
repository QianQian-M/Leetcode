#DFS

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c, key):
            if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = key
                return 1 + dfs(r - 1, c, key) + dfs(r, c + 1, key) + dfs(r + 1, c, key) + dfs(r, c - 1, key)
            return 0
        
        res, n, areas, key = 0, len(grid), dict(), 2
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    areas[key] = dfs(r, c, key)
                    res = max(res, areas[key])
                    key += 1
        
        for r in range(n):
            for c in range(n):
                if not grid[r][c]:
                    neighbors = set()
                    for nr, nc in (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1):
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            neighbors.add(grid[nr][nc])
                    res = max(res, 1 + sum(areas[key] for key in neighbors))
        
        return res