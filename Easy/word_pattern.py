def wordPattern(pattern, strng):
        res=strng.split()
        return list(map(pattern.index, pattern)) == list(map(res.index,res))
