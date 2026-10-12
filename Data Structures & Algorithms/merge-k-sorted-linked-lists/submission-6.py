# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:

    def __init__(self,n : ListNode):
        self.node = n

    
    def __lt__(self,other):

        return self.node.val < other.node.val



    


class Solution:    

    def mergeKLists(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        min_heap = []
        
        dummy_node = ListNode(0,None)
        res = dummy_node

        for lst in lists:
            if lst:
                heapq.heappush(min_heap,NodeWrapper(lst))

        while min_heap:

            node_wrapper = heapq.heappop(min_heap)

            node = node_wrapper.node

            res.next = node
            res = res.next

            node = node.next

            if node:
                heapq.heappush(min_heap,NodeWrapper(node))

        return dummy_node.next


            
    
        