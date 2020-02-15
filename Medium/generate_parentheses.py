def generateParenthesis(n):
        res = []
        def helper(current, left, right):
            if right == 0:
                res.append(current)
            else:
                if left>0:
                    helper(current+"(", left-1, right)
                if left<right:
                    helper(current+")", left, right-1)
        
        helper("",n,n)
        return res
