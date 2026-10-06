class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        find the pair d1, d2 that maximizes p[d2] - p[d1], 
        constraint: d2 must > d1
        if no profit possible (if only negative diffs), ret 0

        if/elif handles never buying and selling on same day,
        and never selling before buying
        """
        # if not prices or len(prices) == 1:
        #     return 0

        min_buy = 0 # running min buy
        profit = 0

        for p in range(1, len(prices)):
            if prices[p] < prices[min_buy]:
                min_buy = p
            elif prices[p] - prices[min_buy] > profit:
                profit = prices[p] - prices[min_buy]

        return profit