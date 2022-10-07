class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next
            
            result.next = ListNode(excess%10)
            result = result.next
            excess = excess//10
            
        return root.next