class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n>=2*m or m==0:
            return 0
        else:
            result = m
            for i in range(m+1, n+1):
                result = result & i
                if result == 0:
                    return 0
            return result
