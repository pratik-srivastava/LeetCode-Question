# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head=ListNode(0)
        small=small_head
        high_head=ListNode(0)
        high=high_head
        while(head!= None):
            if (head.val<x):
                small.next=head
                small=small.next
            else:
                high.next=head
                high=high.next
            head=head.next
        high.next=None
        small.next=high_head.next
        return small_head.next
            
        