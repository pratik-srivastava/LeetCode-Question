# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = rtree = TreeNode()
        
        def inorder(node):
            nonlocal rtree
            if node:
                inorder(node.left)
                rtree.right = TreeNode(node.val)
                rtree = rtree.right
                inorder(node.right)
        
        inorder(root)
        
        return dummy.right
