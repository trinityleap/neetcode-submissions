class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i] = is position i in s reachable using word in wordDict
            can the first i char of s be segmented
        """
        if not s or not wordDict:
            return False

        if len(s) == 1:
            return s in wordDict

        dp = [False] * (len(s) + 1)

        dp[0] = True
        dp[1] = s[:1] in wordDict

        for c in range(2, len(s) + 1):
            for i in range(0, c):
                if dp[i]:
                    sub = s[i:c]
                    if sub in wordDict:
                        dp[c] = True

        return dp[len(s)]