# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #root.left.val is value, not root.left which is node
        #if root.left = None: root.left.val is False
        #traverse: search nodes in different orders here is DFS
        #equivalent = val and structure true
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
