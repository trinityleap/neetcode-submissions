class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        at each step, my choice is between 
            buy (if not holding) 
            and sell
            or do nothing?

        dp[i] max profit through prices[i]

        holding true if holding stock (cannot buy, can sell)
            false if not holding (can buy)
        """

        if not prices or len(prices) == 1:
            return 0

        profit = 0

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]

        return profit