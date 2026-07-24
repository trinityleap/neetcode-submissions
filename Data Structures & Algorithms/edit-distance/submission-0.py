class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j] = min number of operations to 
            make equal word1's first i letters, 
            and word2's first j letters
        
        decision at each iteration:
            can performing one of these op 
            make the strings equal thru i and j
        """
        # base
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        # instantiate dp w initial values 0
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # base cases
        for i in range(m+1):
            dp[i][0] = i  # cost to delete i characters from word1
        for j in range(n+1):
            dp[0][j] = j  # cost to insert j characters into word1

        # construction of dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                # if letter i in 1 equal letter j in 2
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # apply one operation, take min of all three cases
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[m][n]
