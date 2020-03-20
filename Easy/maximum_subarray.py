 def maxSubArray(nums):
        l = g = float("-inf")
        for i in nums:
            l = max(l+i,i)
            g = max(g,l)
        return g      
