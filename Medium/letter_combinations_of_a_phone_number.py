def letterCombinations(digits):
        d = dict(zip('23456789', ['abc','def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']))
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(d[digits[0]])
        prev = letterCombinations(digits[:-1])
        last = list(d[digits[-1]])
        res = [s+c for s in prev for c in last]
        return res
