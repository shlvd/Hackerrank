def rotate(nums, k):
        length = len(nums)
        k = k % length
        i = 0
        count = 0
        while count < length:
            pos = (i + k) % length
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < length:
                pos = (j + k) % length
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1
