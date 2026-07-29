class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
       """
        dp[i] = num distinct combinations that total up to i for 0 <= i <= amount

        combinations NOT permutations -> 1, 2 and 2, 1 don't count separately
       """ 
       dp = [0] * (amount + 1)
       dp[0] = 1  # one way to make amount 0: use no coins
       
       for coin in coins:
           for i in range(coin, amount + 1):
               dp[i] += dp[i - coin]

       return dp[amount]