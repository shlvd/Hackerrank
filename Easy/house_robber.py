def rob(nums):
        N = len(nums)
        dp = [0] * N
        ans = 0
        for i in range(N):
            dp[i] = max(i > 1 and dp[i-2], i > 2 and dp[i-3]) + nums[i]
            ans = max(ans, dp[i])
        return ans
