# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        self.dfs(root, [])
        return self.ans

    def dfs(self, node: TreeNode, current: List[str]):
        if not node:
            return
        current.append(str(node.val))  # 加入当前节点
        if not node.left and not node.right:
            self.ans.append('->'.join(current))
        if node.left:
            self.dfs(node.left, current.copy())  # 注意要加上copy，不然传进去的一直是同一个列表对象
        if node.right:
            self.dfs(node.right, current.copy())
        current = current[:-1]  # 回退