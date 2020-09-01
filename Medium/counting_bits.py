def countBits(num):
        res = []
        for i in range(num + 1):
            res.append(bin(i).count('1'))
        return res
