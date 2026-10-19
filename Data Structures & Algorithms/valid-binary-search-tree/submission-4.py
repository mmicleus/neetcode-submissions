# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # def allSmaller(self,root,value):
    #     if not root:
    #         return True

    #     if root.val < value:
    #         return self.allSmaller(root.left,value) and self.allSmaller(root.right,value)
    #     else:
    #         return False



    # def allLarger(self,root,value):
    #     if not root:
    #         return True

    #     if root.val > value:
    #         return self.allLarger(root.left,value) and self.allLarger(root.right,value)
    #     else:
    #         return False

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

        
        
