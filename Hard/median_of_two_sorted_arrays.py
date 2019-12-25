def findMedianSortedArrays(nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n :
            return self.findMedianSortedArrays(nums2, nums1)
        k = int((m + n - 1) / 2)
        l = 0
        r = min(m, k)
        while l < r:
            midNums1 = int((l + r) / 2)
            midNums2 = int(k - midNums1)
            if nums1[midNums1] < nums2[midNums2]:
                l += 1
            else:
                r = midNums1
        a = max(nums1[l-1] if l > 0  else float('-inf'), nums2[k-l] if k-l >= 0 else float('-inf'))
        if (m + n) & 1 == 1:
            return a
        b = min(nums1[l] if l < m else float('inf'), nums2[k-l+1] if k-l+1 < n else float('inf'))
        return (a+b)/2.0
