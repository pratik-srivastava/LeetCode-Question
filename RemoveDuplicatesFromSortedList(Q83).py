class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        
        while (temp):
            if temp.next and temp.next.val == temp.val:
                temp.next=temp.next.next
            else:
                temp = temp.next
                
        return head
    
