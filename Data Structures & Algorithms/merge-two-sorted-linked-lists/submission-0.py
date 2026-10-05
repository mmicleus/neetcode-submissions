# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = None
        aux = None

        while list1 or list2:

            if not list2:
                newNode = ListNode(list1.val)
                list1 = list1.next
            elif not list1:
                newNode = ListNode(list2.val)
                list2 = list2.next
            elif list1.val < list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next


            if aux:
                aux.next = newNode
                aux = newNode
            else:
                res = aux = newNode

        return res
            
            
        