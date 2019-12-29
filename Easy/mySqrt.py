 def mySqrt(x):
        lo, hi = 0, x
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if mid*mid > x:
                hi = mid - 1
            else:
                lo = mid
        return hi if hi*hi <= x else lo
