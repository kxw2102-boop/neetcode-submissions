# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return sametree(p.right,q.right) and sametree(p.left,q.left)

        if subRoot is None:
            return True

        if root is None:
            return False

        if sametree(root,subRoot):
            return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)




        #def solve(node):

    # 1. Base case
    #if node is None:
        #return ...

    # 2. 对当前节点进行操作
    #...

    # 3. Recursion
    #left = solve(node.left)
    #right = solve(node.right)

    # 4. 合并结果
    #return ...