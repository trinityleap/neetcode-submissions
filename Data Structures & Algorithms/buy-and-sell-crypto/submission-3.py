class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        find the pair d1, d2 that maximizes p[d2] - p[d1], 
        constraint: d2 must > d1
        if no profit possible (if only negative diffs), ret 0
        """

        profit = 0
        buy = 0 # buy day

        for i in range(1, len(prices)):
            if  prices[i] < prices[buy]:
                buy = i
            elif prices[i] - prices[buy] > profit:
                    profit = prices[i] - prices[buy]

        return profit