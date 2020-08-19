def isPowerOfFour(num):
        if num<=0:
            return False
        return num&(num-1)==0 and (num>>1)&(0x55555555)==0
