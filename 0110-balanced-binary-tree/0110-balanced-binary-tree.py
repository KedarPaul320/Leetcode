# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def max_Depth(self,root):
        if root is None :
            return False 
        left_Height = self.max_Depth(root.left)
        right_Height = self.max_Depth(root.right)

        if abs(left_Height - right_Height) > 1 :
            self.ans = False 
        return max(left_Height , right_Height) +1

    def isBalanced(self, root: TreeNode | None) -> bool:
        self.max_Depth(root)
        return self.ans
       
        