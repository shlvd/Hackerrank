def reverseString(s):
        half, count = len(s) // 2, len(s) - 1
        for i in range(half):
            s[i], s[count - i] = s[count - i], s[i]
