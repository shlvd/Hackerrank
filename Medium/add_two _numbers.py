def addTwoNumbers(l1, l2):
        val = l1.val + l2.val;    high = 0;     c = 1;
        if(val > 9):
            high = 1;
            val -= 10;

        res = ListNode(val)
        start = res

        while(l1.next != None or l2.next != None or high == 1):
            tem = high; high = 0

            if(l1.next != None):  
                l1 = l1.next
                tem += l1.val

            if(l2.next != None):
                l2 = l2.next
                tem += l2.val

            if(tem > 9):
                tem -= 10
                high = 1

            res.next = ListNode(tem)
            res = res.next
        return start
