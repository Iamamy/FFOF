# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack=[]
        result=[]
        p=root
        while p or stack:
            while p:
                stack.append([p,0])
                p=p.left
            if stack:
                top=stack.pop()
                if top[1]==1:
                    result.append(top[0].val)
                elif top[0].right:
                    p=top[0].right
                    stack.append([top[0],1])
                else:
                    result.append(top[0].val)
        
        return result
