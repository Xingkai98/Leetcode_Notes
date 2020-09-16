class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        ans = []
        self.recursion(ans, [])
        return ans

    def recursion(self, ans: List[List[int]], current: List[int]):
        if len(current) == self.k:
            ans.append(current)
        if len(current) == 0:
            for _ in range(1, self.n+1):
                self.recursion(ans, current+[_])
            return
        for i in range(current[-1], self.n+1):
            if i not in current:
                self.recursion(ans, current+[i])