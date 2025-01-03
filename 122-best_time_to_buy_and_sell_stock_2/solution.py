class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        start_price = prices[0]
        len_prices = len(prices)
        for i in range(0, len_prices):
            if start_price < prices[i]: 
                max_profit += prices[i] - start_price
            start_price = prices[i]
        return max_profit