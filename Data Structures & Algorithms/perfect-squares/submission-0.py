class Solution:
    def numSquares(self, n: int) -> int:
        from math import isqrt
        """
        coin change reference
        
        dp[i] = minimum squares needed to make num i
            0 <= i <= n
        
        dp[0] = 0
        for each i
            dp[i] = min(dp[i-c] + 1 for each coin where c <= i
                 and dp[i-c] != float('inf')), default=float('inf'))

        return dp[amount] if dp[amount] != float('inf') else -1

        i  1 2 3 4 5 6
        dp 1 2 3 1 2 3
        """

        if not n or n == 0:
            return 0

        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            # 
            dp[i] = min(dp[i-s*s] + 1 for s in range(1, isqrt(i)+1))

        return dp[n]