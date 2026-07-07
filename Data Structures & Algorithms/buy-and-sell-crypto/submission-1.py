class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0 # difference btwn highest sell and lowest buy
        sell = 0
        buy = prices[0]
        for n in prices: # loop over prices
            # if price gives better profit update
            if n < buy: # if found better buy price update
                buy = n
            elif n - buy > max: # if found better sell price
                sell = n
                max = sell - buy # update max profit
            
        return max if max > 0 else 0