class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs','tuv','wxyz']
        result = []
        for index, digit in enumerate(digits):
            if index == 0:
                result += [char for char in letters[int(digit)]]
            else:
                result = [a+b for a in result for b in letters[int(digit)]]
        return result
