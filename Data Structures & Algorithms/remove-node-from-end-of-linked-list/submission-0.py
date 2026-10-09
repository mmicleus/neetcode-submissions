# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self,head: Optional[ListNode], n: int) -> Optional[ListNode]:


        if not head:
            return None

        
        tail = head
        count = 0

        while tail:
            count += 1
            tail = tail.next


        

        indexToRemove = count - n

        extraHead = ListNode()

        extraHead.next = head

        head = extraHead


        tail = head

        i = 0

        while i < indexToRemove:
            tail = tail.next
            i += 1

        
        tail.next = tail.next.next


        return head.next
        