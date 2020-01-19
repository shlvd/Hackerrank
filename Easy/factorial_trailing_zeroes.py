def trailingZeroes(n):
        assert n >= 0, n
        zeros = 0
        q = n

        while q:
            q //= 5
            zeros += q

        return zeros
