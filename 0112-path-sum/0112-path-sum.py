# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        # Helper function for Depth First Search (DFS) tracking the accumulated sum
        def dfs(node, currSum):
            # Base Case 1: If we reach a null child, this path is invalid
            if not node:
                return False
            
            # Add the current node's value to our path sum runner
            currSum += node.val 
            
            # Base Case 2: If it's a leaf node (no children), check if the sum matches targetSum
            if not node.left and not node.right:
                return currSum == targetSum
            
            # Recursively explore the left and right subtrees
            # Returns True if either branch finds a valid root-to-leaf path sum
            return (dfs(node.left, currSum) or 
                    dfs(node.right, currSum))
        
        # Start the traversal from the root node with an initial sum of 0
        return dfs(root, 0)
