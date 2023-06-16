class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # checking when no profit is possible
        reverse = sorted(prices, reverse=True)
        if reverse == prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, (price - min_price))
        return max_profit