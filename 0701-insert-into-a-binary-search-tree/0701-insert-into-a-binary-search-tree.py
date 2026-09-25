# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        new_node = TreeNode(val)
        if root is None :
            return new_node 
        curr = root 
        while curr != None :
            if val < curr.val :
                if curr.left != None :
                    curr = curr.left 
                else :
                    curr.left = new_node 
                    break 
            else:
                if curr.right != None :
                    curr = curr.right 
                else :
                    curr.right = new_node 
                    break 
        return root 
        