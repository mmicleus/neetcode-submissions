# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST2(self,root: Optional[TreeNode],minim,maxim) -> bool:

        if not root:
            return True

        if minim and root.val < minim:
            return False

        if maxim and root.val > maxim:
            return False

        if root.left and root.left.val >= root.val:
            return False
        
        if root.right and root.right.val <= root.val:
            return False

        
        return self.isValidBST2(root.left,minim,root.val - 1) and self.isValidBST2(root.right,root.val + 1,maxim)
        






    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        return self.isValidBST2(root,None,None)

        
        
