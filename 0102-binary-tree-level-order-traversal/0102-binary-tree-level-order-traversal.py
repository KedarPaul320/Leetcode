# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        # Return an empty list immediately if the tree is completely empty
        if not root:
            return []

        # Initialize the main list that will hold lists of values for each level
        ans = []
        # Initialize a double-ended queue (deque) starting with the root node
        queue = deque([root])

        # Continue traversing as long as there are nodes left in the queue
        while queue:
            # Create a temporary list to store node values for the current level
            level = []
            # Find the exact number of nodes present at the current level
            size = len(queue)

            # Process all nodes that belong strictly to the current level
            for _ in range(size):
                # Remove and retrieve the front node from the queue
                node = queue.popleft()
                # Append the retrieved node's value to the current level list
                level.append(node.val)

                # If a left child exists, add it to the queue for the next level
                if node.left:
                    queue.append(node.left)
                # If a right child exists, add it to the queue for the next level
                if node.right:
                    queue.append(node.right)

            # Append the completed level list to the main answer list
            ans.append(level)

        # Return the full multi-level list of node values
        return ans
