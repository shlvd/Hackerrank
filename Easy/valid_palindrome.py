def isPalindrome(s):
        table = str.maketrans(dict.fromkeys(string.punctuation))  
        new_s = s.translate(table).replace(" ", "").lower()
        return new_s == new_s[::-1]
