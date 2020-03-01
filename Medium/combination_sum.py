def combinationSum(candidates, target):
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for c in candidates:
            for comb_sum in range(target + 1):
                if dp[comb_sum] and comb_sum + c <= target:
                    dp[comb_sum + c].extend([comb + [c] for comb in dp[comb_sum]])
        return dp[target]
