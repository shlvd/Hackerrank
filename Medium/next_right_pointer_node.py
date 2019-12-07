def connect(root):
        if root == None: return root
        prev = root
        head = None
        while prev.left != None:
            while prev != None:
                if head == None:
                    head = prev.left
                    curr = prev.left
                else:
                    curr.next = prev.left
                    curr = curr.next
                curr.next = prev.right
                prev = prev.next
                curr = curr.next
            prev = head
            head = None
        return root
