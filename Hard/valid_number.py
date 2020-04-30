def isNumber(s):
        # trim whitespaces
        s= s.strip()
        # false if empty
        if len(s) == 0:
            return False
        # keep track of position, # of digits, # of dot
        pt = num = dot = 0
        # skip signs only once
        if s[pt] == '+' or s[pt] == '-':
            pt += 1
        while pt < len(s):
            # count digits
            if s[pt]>='0' and s[pt]<='9':
                pt += 1
                num += 1
            # count dots
            elif s[pt] == '.':
                pt += 1
                dot += 1
            # if not digit or dot, invalid and break
            else:
                break
        # no digits between the 1st sign and next non-digit non-dot char, or more than 1 dot
        if num == 0 or dot > 1:
            return False
        # if reaches end, true
        if pt == len(s):
            return True
        # if not dot, not digit, not e, false
        elif pt < len(s) and s[pt] != 'e':
            return False
        else:
            pt += 1
        # if it's e, check after e    
        num = 0
        # skip first sign after e
        if pt< len(s) and s[pt] in ['+','-']:
            pt += 1
        # skip all digits and count
        while pt < len(s) and s[pt]>='0' and s[pt]<='9':
            pt += 1
            num += 1
        # if between e and the end are not more than 1 digits, false
        if num == 0 or pt != len(s):
            return False
        return True
