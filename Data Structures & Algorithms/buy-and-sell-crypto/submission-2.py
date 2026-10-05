class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        find the pair d1, d2 that maximizes p[d2] - p[d1], 
        constraint: d2 must > d1
        if no profit possible (if only negative diffs), ret 0
        """

        profit = 0

        for i in range(0, len(prices) - 1): # buy
            for j in range(i + 1, len(prices)): # sell
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        return profit