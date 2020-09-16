# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        d = dict()
        self.dfs(root, d, 0)
        ans = []
        for each_depth in d:
            ans.append(d[each_depth])
        ans.reverse()
        return ans

    def dfs(self, node: TreeNode, depths: dict, current: int) -> dict:  # current表示进该节点之前的深度
        if not node:
            return
        current += 1
        if current not in depths:
            depths[current] = []
        depths[current].append(node.val)
        if node.left:
            self.dfs(node.left, depths, current)
        if node.right:
            self.dfs(node.right, depths, current)

