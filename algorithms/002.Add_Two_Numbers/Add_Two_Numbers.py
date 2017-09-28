class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cur1 = l1
        cur2 = l2
        flag = False
        while cur1 or cur2:
            sum = 0
            if flag:
                sum += 1
            sum += cur1.val + cur2.val
            if sum > 9:
                sum -= 10
                flag = True
            else:
                flag = False
            cur1.val = sum
            if cur1.next is None and cur2.next is None:
                if flag:
                    cur1.next = ListNode(1)
                    return l1
                else:
                    return l1
            elif cur1.next is None and cur2.next is not None:
                cur1.next = cur2.next
                while cur2.next:
                    if flag:
                        cur2.next.val += 1
                        if cur2.next.val > 9:
                            cur2.next.val -= 10
                            flag = True
                        else:
                            flag = False
                    cur2 = cur2.next
                if flag:
                    cur2.next = ListNode(1)
                    return l1
                else:
                    return l1
            elif cur1.next is not None and cur2.next is None:
                while cur1.next:
                    if flag:
                        cur1.next.val += 1
                        if cur1.next.val > 9:
                            cur1.next.val -= 10
                            flag = True
                        else:
                            flag = False
                    # tmp = cur1
                    cur1 = cur1.next
                if flag:
                    cur1.next = ListNode(1)
                return l1
            else:
                cur1 = cur1.next
                cur2 = cur2.next
        return l1
