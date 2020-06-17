def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        curr = n
        lis = []
        nums = []
        nums.append(curr)
        while curr != 1:
            for i in range(len(str(curr))):
                lis.append(math.pow(int(str(curr)[i]), 2))
            curr = sum(map(int, lis)) 
            lis = []
            if curr == 1:
                return True
            elif curr in nums:
                return False
            nums.append(curr)
