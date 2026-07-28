class Solution:
    def numSquares(self, n: int) -> int:
        """
        1d dynamic lookback?

        dp[i] = least num square nums that sum to i, for 0 <= i <= n
        recurrence: 

        1 4 9 16 25 36

        1 2 3 4 5 6 7 8 9 10
        1 2 3 1 2 3 4 5 1 2
        """
        # bases

        dp = [float('inf')] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = 1 + min(dp[i- s*s] for s in range(math.isqrt(i) + 1))

        return dp[n]