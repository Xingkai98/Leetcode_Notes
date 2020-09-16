class Solution:
    def sums(self, num: int) -> int:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s

    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:
            return 1
        visited = [[0 for i in range(n)] for j in range(m)]
        a = self.dfs(0, 0, m, n, k, visited)
        return a

    def dfs(self, i: int, j: int, m: int, n: int, k: int, visited) -> int:
        if i >= m or j >= n or self.sums(i) + self.sums(j) > k or visited[i][j]>0:
            return 0
        ans = 1
        if i + 1 < m and self.sums(i+1) + self.sums(j) <= k:   # 向下
            ans += self.dfs(i + 1, j, m, n, k, visited)
        if j + 1 < n and self.sums(i) + self.sums(j+1) <= k:   # 向右
            ans += self.dfs(i, j + 1, m, n, k, visited)
        visited[i][j] = 1
        # print(str(i) + ' ' + str(j) + ' ' + str(ans))
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.sums(377))
    print(s.movingCount(5, 6, 5))

# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
