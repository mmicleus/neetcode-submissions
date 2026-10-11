# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def insort_desc(self,lst, x):
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid].val > x.val:     # use >= for "insert before equals"
                lo = mid + 1
            else:
                hi = mid
        lst.insert(lo, x)


    def mergeKLists(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        lists = [x for x in lists if x ]

        lists.sort(key = lambda node : node.val,reverse=True)


        head = ListNode(0)
        tailSortedList = head

        while len(lists) > 0:

            # get the node with the smalllest value
            node = lists[-1]

            # add node to the sorted list
            tailSortedList.next = node

            tailSortedList = node


            node = node.next

            #if all elements of the current linked list have been added, then remove it from "lists"
            if not node:
                lists.pop()

            else:
                lists.pop()
                #reorder "lists"
                self.insort_desc(lists,node)


        return head.next
        