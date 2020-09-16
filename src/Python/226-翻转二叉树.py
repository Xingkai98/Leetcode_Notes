# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        new_node = TreeNode()
        self.construct(root, new_node)
        return new_node

    def construct(self, node: TreeNode, new_node: TreeNode) -> TreeNode:
        new_node.val = node.val
        if node.left:
            right = TreeNode()
            new_node.right = right
            self.construct(node.left, right)
        if node.right:
            left = TreeNode()
            new_node.left = left
            self.construct(node.right, left)


