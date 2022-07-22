# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            rev = ListNode(head.val, rev)
            head = head.next
        return rev