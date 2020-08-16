def maxProfit(prices):
        sold = 0
        rest = 0
        hold = -float('inf')
        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)
        return max(rest, sold)
