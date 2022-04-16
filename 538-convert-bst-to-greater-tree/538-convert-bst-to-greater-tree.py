# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode],val:int)->int:
            if not node: return val
            node.val+=dfs(node.right,val)
            return dfs(node.left,node.val)
        sum=dfs(root,0)
        return root
