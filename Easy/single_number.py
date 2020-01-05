def singleNumber(nums):
        result = 0
        for i in nums:
            result ^= i
        return result
