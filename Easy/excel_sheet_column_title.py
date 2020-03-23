def convertToTitle(n):
        r = ''
        while n > 0:
            [n, i] = divmod(n - 1, 26)
            r = chr(65 + i) + r
        return r
