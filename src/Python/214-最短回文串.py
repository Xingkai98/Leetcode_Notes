class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ans = 0  # 从左到右最多到哪里是回文
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                ans = i
        return s[ans + 1:][::-1] + s

    def isPalindrome(self, s: str) -> bool:
        return s[::-1] == s