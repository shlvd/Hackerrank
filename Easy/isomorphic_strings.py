def isIsomorphic(s, t):
        dic={}
        for i,x in enumerate(s):
            if x in dic.keys() and dic[x]!=t[i]:
                return  False
            elif x not in dic.keys() and t[i] in dic.values():
                return False
            else:
                dic[x]=t[i]
                
        return True
