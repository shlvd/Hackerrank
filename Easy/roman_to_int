def romanToInt(s):
        d = {"M":1000, "D": 500, "C": 100,"L":50, "X":10, "V": 5, "I":1}
        result = d[s[-1]]
        r = [-d[s[i]] if d[s[i]] < d[s[i + 1]] else d[s[i]] for i in range(len(s) - 2, -1, -1)]
        return result + sum(r)
