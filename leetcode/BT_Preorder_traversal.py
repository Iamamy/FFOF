# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        p=root
        stack=[]
        result=[]
        while p or stack:
            while p:
                result.append(p.val)
                stack.append(p)
                p=p.left
            if stack:
                p=stack.pop()
                p=p.right
        
        return result