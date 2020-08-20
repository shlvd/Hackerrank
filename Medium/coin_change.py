 def coinChange(coins, amount):
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] >= amount + 1:
            return -1
        else:
            return dp[amount]
