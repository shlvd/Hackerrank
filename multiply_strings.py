class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0:
            return ""

        n1 = len(num1)
        n2 = len(num2)

        # Reverse the string so we can scan strings from the left to right
        # T(n) = O(n)
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Create an empty ret string
        # S(n) = O(n)
        ret = [0] * (n1 + n2)

        # For each digits in s2
        for j in range(n2):
            carry = 0
            d2 = int(num2[j])

            # Calculate s1 * d2
            for i in range(n1):
                d1 = int(num1[i])
                res = ret[i+j] + d1 *d2 + carry
                carry = int(res / 10)
                ret[i+j] = res - carry * 10

            # After calculation of s1*d2, we need to check if s1 * d2 has a carry at the highest position
            # We can assume that it is the first time to visit ret[n1 + j]
            if carry != 0:
                ret[n1 + j] = carry

        # Convert result from int to string, and reverse the digits
        ret = "".join(str(x) for x in ret[::-1])
        i = 0
        while i < len(ret) and ret[i] == '0':
            i += 1
        ret = ret[i:]
        if len(ret) == 0: return '0'
        return ret
