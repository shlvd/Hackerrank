def reverseWords(s):
        listOfWords = [elem for elem in s.strip().split() if elem != ' ']
        listOfWords.reverse()
        return ' '.join(listOfWords)
