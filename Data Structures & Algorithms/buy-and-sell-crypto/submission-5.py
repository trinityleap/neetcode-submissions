class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        find the pair d1, d2 that maximizes p[d2] - p[d1], 
        constraint: d2 must > d1
        if no profit possible (if only negative diffs), ret 0

        if/elif handles never buying and selling on same day,
        and never selling before buying
        """
        min_buy = prices[0] # running min buy price
        profit = 0

        for p in prices:
            if p < min_buy:
                min_buy = p
            elif p - min_buy > profit:
                profit = p - min_buy

        return profit