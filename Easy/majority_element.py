def majorityElement(nums):
        digits = {}
        for i in nums:
            digits[i] = digits.get(i, 0) + 1
            if digits[i] > len(nums)/2:
                return i
