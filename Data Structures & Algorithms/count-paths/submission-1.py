class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[i][j] = num unique paths that can be taken from top left corner to grid[i][j] 
            for 0 <= i, j < m, n

        initial values: first row and first column all 1

        dp = from left + from up
        """
        dp = [[0] * (n) for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]