def restoreIpAddresses(s):
        if not s or len(s) < 4:
            return []
        
        res = []
        dfs(s, [], res)
        return res
        
    def dfs(s, path, res):
        if path and s == '' and len(path) == 4:
            res.append('.'.join(path))
            return
        
        if path and len(path) > 4:
            return
        
        for i in range(3):
            if i < len(s) and int(s[:i+1]) <= 255:
                if s[:i+1].startswith('0') and i >= 1:
                    continue
                self.dfs(s[i+1:], path+[s[:i+1]], res)
        
