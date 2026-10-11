# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
  
    def reorderList(self,head: Optional[ListNode]) -> None:

        l = head
        r = head.next

        while r and r.next:
            l = l.next
            r = r.next.next


        secondHalf = l.next
        prev = l.next = None


        while secondHalf:

            aux = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = aux

        secondHalf = prev


        while secondHalf:
            
            aux1 = head.next

            head.next = secondHalf
            aux2 = secondHalf.next
            secondHalf.next = aux1

            head = aux1
            secondHalf = aux2


        
