def strStr(haystack, needle):
        if needle=="" :
            return 0
        if len(needle)>len(haystack) :
            return -1

        for i in range(len(haystack)) :
            if haystack[i:i+len(needle)]==needle :
                return i
        return -1
