def searchInsert(nums, target):
        nums.append(target)         
        nums.sort()                 
        for i,j in enumerate(nums): 
            if target == j:         
                return i      
