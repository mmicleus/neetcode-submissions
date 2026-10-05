# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        refs = []

        while head and head not in refs:

            refs.append(head)
            head = head.next

        return True if head else False
        