#COPIED and PASTED Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def helper(root):
            """
            param type root: TreeNode
                  rtype root
            """
            if not root:
                return
            
            left_end = helper(root.left)
            right_end = helper(root.right)
            
            if left_end:
                
                left_end.right = root.right
                root.right = root.left
                root.left = None
                
            end_pointer = right_end or left_end or root
            
            return end_pointer
        
        helper(root)