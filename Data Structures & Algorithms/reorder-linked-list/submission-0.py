# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def getNumberOfNodes(self,head):

        aux = head
        count = 0

        while aux:
            count += 1
            aux = aux.next

        return count


    def getNodeX(self,head:ListNode,x:int):
    
        nodeX = head
        x -= 1

        while x > 0:
            nodeX = nodeX.next
            x -= 1

        return nodeX


  
    def reorderList(self,head: Optional[ListNode]) -> None:

        nodeCount = self.getNumberOfNodes(head)

        #storing a reference to the head of the resulting linked list
        res = head

        while nodeCount > 1:

            aux = head.next

            head.next = self.getNodeX(head,nodeCount)

            print(head.next.val)

            if nodeCount > 2:
                head.next.next = aux
                print(head.next.next.val)
            else:
                head.next.next = None

            

            head = aux

            nodeCount -= 2

        head.next = None

        # return res
        