def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        
        lt=-1
        gt=n
        i=0
        while i<gt:
            if nums[i]==1:
                i+=1
            elif nums[i]<1:
                if i!=lt+1:
                    nums[lt+1],nums[i]=nums[i],nums[lt+1]
                lt+=1
                i+=1
            elif nums[i]>1:
                if i!=gt-1:
                    nums[gt-1],nums[i]=nums[i],nums[gt-1]
                gt-=1
