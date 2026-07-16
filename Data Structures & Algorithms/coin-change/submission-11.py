class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        
        if amount == 0:
            return 0

        if len(coins) == 1:
            if coins[0] > amount: 
                return -1
            if amount < coins[0]:
                if amount % coins[0] == 0:
                    return amount // coins[0]
                return -1
            if amount == coins[0]:
                return 1
        
        """
        dp[i] = minimum coins needed to make amount i
            0 <= i <= amount
        
        dp[0] = 0
        for each i
            dp[i] = min(dp[i-c] + 1 for each coin where c <= i)
        """

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount+1):
            dp[i] = min((dp[i-c]+1 for c in coins if c <= i and dp[i-c] != float('inf')), default=float('inf'))

        return dp[amount] if dp[amount] != float('inf') else -1
