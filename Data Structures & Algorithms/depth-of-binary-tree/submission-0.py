# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:

    def __init__(self):
        self.depth = 0

    

    def traverse(self,root: Optional[TreeNode],count:int):
        
    

        if not root:
            self.depth = max(count,self.depth)
            return

        count += 1

        self.traverse(root.left,count)
        self.traverse(root.right,count)

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.traverse(root,0)

        return self.depth
        