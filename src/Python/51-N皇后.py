class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.ans = []
        self.recursion('', [i for i in range(n)])
        # print(self.ans)
        return self.construct_ans(self.ans)

    def construct_ans(self, l: List[str]) -> List[List[str]]:  # 由字符串得到最终结果
        result = []
        for each in l:
            tmp = []
            for char in each:
                tmp.append('.' * (int(char)) + 'Q' + '.' * (self.n - 1 - int(char)))
            result.append(tmp)
        return result

    def recursion(self, s: str, candidate: List[str]):  # 以字符串的形式先进行推演
        # print(s)
        # print(candidate)
        if len(s) == self.n:
            self.ans.append(s)
            return
        for c in candidate:
            # print(str(c) + ' chosen')
            unavailable = [str(c)] + [str(int(c) - 1)] + [str(int(c) + 1)]
            if len(s) > 0:
                unavailable += list(s)
            for index, ch in enumerate(s):
                distance = len(s) + 1 - index
                unavailable += [str(int(ch) + distance), str(int(ch) - distance)]
            unavailable = list(set(unavailable))  # 找出这一行不能放棋子的位置
            # print('unavailable: '+str(unavailable))
            self.recursion(s + str(c), [str(i) for i in range(self.n) if str(i) not in unavailable])