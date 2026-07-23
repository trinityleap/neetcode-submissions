class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        similar to number of islands, but rather than tracking count of islands, 
            track biggest island area seen, update for each new island as discovered
        """
        area = 0

        def dfs(r, c):
            # if out of bounds
            if r >= len(grid) or r < 0:
                return 0
            elif c >= len(grid[0]) or c < 0:
                return 0
            
            # if already visited
            if grid[r][c] != 1:
                return 0

            # if visitng mark visited and update curr area
            grid[r][c] = 0

            # explore immediate neighbors
            return (1 + 
                        dfs(r-1, c) +
                        dfs(r+1, c) +
                        dfs(r, c-1) +
                        dfs(r, c+1) 
                    )

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
            
        return area