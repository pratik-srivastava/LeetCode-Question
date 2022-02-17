# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = temp= ListNode()
        while list1 and list2:
            if list1.val>list2.val:
                node.next=list2
                list2=list2.next
            else:
                node.next=list1
                list1=list1.next
            node=node.next
        if not list1:
            node.next=list2
        else:
            node.next=list1
        return temp.next
        
