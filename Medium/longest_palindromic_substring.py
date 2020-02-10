def longestPalindrome(s):
       if len(s) < 2 or s == s[::-1]:
            return s
        longest_pal = ['']
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > 0:
                    longest_pal.append(s[i:j])
                    
        return max(longest_pal, key=len)
