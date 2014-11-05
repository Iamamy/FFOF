# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        p=root
        depth=1
        
        if p:
            l=self.maxDepth(p.left)
            r=self.maxDepth(p.right)
            if l>r:
                depth=depth+l
            else:
                depth=depth+r
            return depth
        else:
            return 0