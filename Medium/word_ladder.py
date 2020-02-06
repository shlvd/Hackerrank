def ladderLength(beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        wordSet = set(wordList)
        
        q = [(beginWord, 1)]
        while q:
            word, length = q.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    trans = word[:i] + char + word[i+1:]
                    if trans in wordSet:
                        wordSet.remove(trans)
                        q.append((trans, length+1))
                        
        return 0
