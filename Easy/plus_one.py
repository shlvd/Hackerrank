def plusOne(digits):
        num = 0
        n = len(digits)      
        for i in range(n):
            num += digits[i] * (10**(n-1-i))
        return [dig for dig in str(num+1)]
