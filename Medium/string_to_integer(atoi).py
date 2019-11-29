def myAtoi(str):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        str = str.lstrip(" ")
        if not str: return 0
        num = str.split(" ")[0]
        result = ""
        if num[0] == "-":
            result += "-"
            num = num[1:]
        elif num[0] == "+": num = num[1:]
        for char in num:
            try:
                x = int(char)
                result += char
            except:
                break
        try:
            result = int(result)
            if result in range(INT_MIN, INT_MAX):
                return result
            else:
                if result < 0: return INT_MIN
                else: return INT_MAX
        except:
            return 0
