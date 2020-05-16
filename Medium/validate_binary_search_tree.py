def isValidBST(root):
        if not root:
            return True
        prev = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        return True
