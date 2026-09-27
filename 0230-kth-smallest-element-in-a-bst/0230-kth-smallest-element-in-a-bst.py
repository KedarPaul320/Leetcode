# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        self.count = 0
    def inorder(self,root,k):
        if root is None :
            return None 
        self.inorder(root.left,k)
        self.count += 1 
        if self.count == k:
            self.ans = root.val
        if self.count < k :
            self.inorder(root.right,k)
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.ans = 0 
        self.inorder(root,k)
        return self.ans

        