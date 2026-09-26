# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,min_limit,max_limit):
        if root is None :
            return True 
        if root.val < min_limit or root.val > max_limit :
            return False 
        check_left = self.check(root.left , min_limit , root.val-1)
        check_right = self.check(root.right , root.val+1 , max_limit)

        return check_left and check_right
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.check(root,float('-inf'),float('inf'))