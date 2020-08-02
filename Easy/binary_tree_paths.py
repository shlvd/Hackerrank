 def binaryTreePaths(root):
        if root is None:
            return []

        res = []
        path = [root]
        prev_node = TreeNode(None)

        while path:
            N = path[-1]
            # Check if N is Leaf
            if N.left is None and N.right is None:
                res.append("->".join([str(x.val) for x in path]))
                prev_node = path.pop()
            else:
                # N is not the leaf, we have three possible options:
                # 1) Go left, if N has a left child and left child is not visited
                # 2) Go right, if N has a right child and (left child is visited or None)
                # 3) Go up, if right (as well as left) child is already visited or None
                if N.right == prev_node:
                    prev_node = path.pop()
                elif N.left == prev_node:
                    if N.right is None:
                        prev_node = path.pop()
                    else:
                        path.append(N.right)
                elif N.left is not None:
                    path.append(N.left)
                elif N.right is not None:
                    path.append(N.right)
