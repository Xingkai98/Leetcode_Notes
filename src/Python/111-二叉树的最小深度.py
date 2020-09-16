# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.dfs(root, 1, 0xFFFF)

    def dfs(self, node: TreeNode, current: int, answer: int) -> int:
        # 是叶节点
        if not node.left and not node.right:
            return min(answer, current)

        # 不是叶节点
        result = 0xFFFF
        if node.left:
            result = min(result, self.dfs(node.left, current + 1, answer))
        if node.right:
            result = min(result, self.dfs(node.right, current + 1, answer))
        return result