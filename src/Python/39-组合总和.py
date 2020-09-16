class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.recursion(candidates, [], target)

    def recursion(self, candidates: List[int], current: List[int], target: int):
        if target == 0:
            return [current]
        ans = []
        if not current:
            startup = [[i] for i in candidates if i <= target]
            for each in startup:
                ans += self.recursion([i for i in candidates if i >= each[0]], each, target - each[0])
        else:
            for c in candidates:
                diff = target - c
                if diff >= 0:
                    ans += self.recursion([i for i in candidates if i >= current[-1] and i >= c], current + [c], diff)
        # print(ans)
        return ans
