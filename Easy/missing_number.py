def missingNumber(nums):
        n = len(nums)
        return int(n*(n+1)/2) - sum(nums) 
