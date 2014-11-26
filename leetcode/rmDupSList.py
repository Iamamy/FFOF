# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head:
            current=head
            while current.next != None:
                head1=current
                head2=current.next
                if head2.val==head1.val:
                    head1.next=head2.next
                    del head2
                else:
                    current=current.next
            return head
        else:
            return head
            


         
                
            
                

        
        