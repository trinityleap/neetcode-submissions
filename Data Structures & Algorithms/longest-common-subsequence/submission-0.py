class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j] is longest common subseq thru the first i in 1 and j in 2
        """
        # base: if strings share no char, return 0
        if set(text1).isdisjoint(text2):
            return 0

        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # dp[0][0], dp[1][0], dp[0][1] = 0, 0, 0
        # if text1[0] == text2[0]:
        #     dp[1] = [1] * len(dp[1])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]