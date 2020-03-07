def permute(nums):
        result = []
        def solve(prefix, suffix):
            if prefix == []:
                result.append(suffix)
            else:
                for i,n in enumerate(prefix):
                    solve(prefix[:i]+prefix[i+1:], suffix+[n])
        
        solve(nums, [])
        return result
