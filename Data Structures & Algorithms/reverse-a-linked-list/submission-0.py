# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        items = []
        res : Optional[ListNode] = None
        result : Optional[ListNode] = None

        while head:
            
            items.append(head.val)

            head = head.next


        for i in range(len(items) - 1, -1, -1):
            
            if not res:
                res = ListNode(items[i])
                result = res
            else:
                res.next = ListNode(items[i])
                res = res.next

        return result


            








        