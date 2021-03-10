def simplifyPath(self, path: str) -> str:
        path_lst = [s for s in path.split('/') if s.strip()]
        stack = []
        for s in path_lst:
            if s == '.':
                continue
            if s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/' + '/'.join(stack)
