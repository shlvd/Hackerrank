def rob(self, nums: List[int]) -> int:
        
        if nums is []:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next
