# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.indices = {x:i for i,x in enumerate(inorder)}

        self.preorder_index = 0


        def dfs(l,r):

            if l > r:
                return None

            root = preorder[self.preorder_index]

            self.preorder_index += 1

            mid = self.indices[root]

            root_node = TreeNode(root)

            root_node.left = dfs(l,mid - 1)
            root_node.right = dfs(mid + 1,r)

            return root_node

        return dfs(0,len(preorder) - 1)





