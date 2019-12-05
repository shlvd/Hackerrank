def countAndSay(n):
        string = '1'
        for i in range(n - 1):
            cnt = 0
            new_string = []
            prev_c = None
            for c in string:
                if prev_c is not None and prev_c != c:
                    new_string.append(str(cnt)+prev_c)
                    cnt = 0
                cnt += 1
                prev_c = c
            new_string.append(str(cnt)+c)
            string = ''.join(new_string)
        return string
