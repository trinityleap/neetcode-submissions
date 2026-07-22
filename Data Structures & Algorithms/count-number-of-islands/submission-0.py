class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 

        def dfs(g, r, c):
            # out of bounds or already visited
            if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]):
                return
            if g[r][c] != '1':
                return

            g[r][c] = '0'  # mark visited
            
            dfs(g, r+1, c)
            dfs(g, r-1, c)
            dfs(g, r, c+1)
            dfs(g, r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':  # found new island
                    count += 1
                    dfs(grid, r, c)  # mark whole island as visited
        
        return count