def myPow(x, n):
        #return x**n
        if n == 0:          return 1                     
        elif n < 0:         return 1.0 / myPow(x, -n) 
        elif n == 1:        return x                     
        else:
            if n % 2 == 0:  return myPow(x*x, n//2)
            else:           return myPow(x*x, n//2)*x
