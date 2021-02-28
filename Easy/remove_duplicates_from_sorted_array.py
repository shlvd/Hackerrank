 def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        
        previous = 0
        for current in range(1,len(nums)):
            if nums[current] != nums[previous]:
                previous += 1
                nums[previous] = nums[current]

        return previous + 1
