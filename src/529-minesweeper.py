class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        self.subUpdateBoard(click[0], click[1], board, visited)
        return board

    def subUpdateBoard(self, x: int, y: int, board: List[List[str]], visited: List[List[str]]) -> List[List[str]]:
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or visited[x][y] == 1:
            return

        visited[x][y] = 1
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return

        # 统计四周雷数
        mine = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == 'M':
                    mine += 1

        if mine == 0:
            board[x][y] = 'B'
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self.subUpdateBoard(i, j, board, visited)
        else:
            board[x][y] = str(mine)

# https://leetcode-cn.com/problems/minesweeper/




