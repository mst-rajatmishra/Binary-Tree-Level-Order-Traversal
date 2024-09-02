from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])  # (node, level)

        while queue:
            node, level = queue.popleft()
            
            # If the current level is not in the result, add it
            if level == len(result):
                result.append([])
            
            # Append the current node's value to its level
            result[level].append(node.val)
            
            # Enqueue the left and right children if they exist
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.levelOrder(root1))  # Output: [[3], [9, 20], [15, 7]]

# Example 2
root2 = TreeNode(1)
print(solution.levelOrder(root2))  # Output: [[1]]

# Example 3
root3 = None
print(solution.levelOrder(root3))  # Output: []
