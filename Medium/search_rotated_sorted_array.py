def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        middle = 0
        while low <= high:
            middle = (low + high)//2
            if target >= nums[0] > nums[middle]:
                nums[middle] = float('inf')
            elif target < nums[0] <= nums[middle]:
                nums[middle] = -1*float('inf')
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return -1
