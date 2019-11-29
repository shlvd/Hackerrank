def longestCommonPrefix(strs):
        grs, l_pre = zip(*strs), ""
        for gr in grs:
            if len(set(gr)) > 1: break
            l_pre += gr[0]
        return l_pre
        #return os.path.commonprefix(strs)
