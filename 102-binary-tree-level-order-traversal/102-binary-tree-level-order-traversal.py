# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs=[]
        if root is None:
            return bfs
        q=deque([])
        q.append(root)
        while len(q)!=0:
            curr=[]
            level_size=len(q)
            for i in range(level_size):
                d=q.popleft()
                curr.append(d.val)
                if d.left is not None:
                    q.append(d.left)
                if d.right is not None:
                    q.append(d.right)
            bfs.append(curr)
        return bfs
                
        