def isValid(s): 
        parentheses = {"[": "]", "{": "}", "(": ")"}
        stack = [] 
        for par in s:
            if par in parentheses:
                stack.append(parentheses[par])
            elif not stack or par != stack.pop():
                return False
        return not stack  
