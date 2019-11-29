def isPalindrome(x):
        return x == int(str(x)[::-1]) if x >= 0 else False
