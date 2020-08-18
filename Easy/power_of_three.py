 def isPowerOfThree(n):
        return False if n <= 0 else n == pow(3, round(math.log(n, 3)))
