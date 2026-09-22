# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(level) > 0 :
                if len(ans) % 2 == 1 :
                    level.reverse()
            ans.append(level)

        return ans
        