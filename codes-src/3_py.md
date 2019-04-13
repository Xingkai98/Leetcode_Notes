### 1
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        ans = 0
        for i in range(0, len(s)):
            l.clear()
            tmp = s[i:]
            for j in tmp:
                if len(l) == 0 or j not in l:
                    l.append(j)
                else:
                    break
            ans = max(ans,len(l))
        return ans
```
#### 数据
Runtime: 1924 ms, faster than 5.01%.<br/>Memory Usage: 13.4 MB, less than 5.05%.<br/>而这一次的代码基本上在速度和空间上都属于垫底水平了，直觉告诉我，最大原因是因为方法太笨了，毕竟是O(n^2)。

### 2 
```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, l, r = 0, 0, 0
        dic = dict()
        while l < len(s) and r < len(s):
            #check if against the rule
            #if it is, l++ until under the rule
            signal = 1
            while signal == 1:
                dic.clear()
                signal = 0
                #这里注意是l到r+1而不是l到r！！
                for i in s[l:r+1]:
                    if i not in dic:
                        dic[i] = 1
                    else:
                        signal = 1
                        l += 1
                        break
            #record
            ans = max(ans, r-l+1)
            r+=1
        return ans
```
#### 数据
Runtime: 656 ms, faster than 12.30%.<br/>Memory Usage: 13.3 MB, less than 5.05%.<br/>出人意料的仍然很慢。不过能够看出来时间从O(n^2)到O(n)的进步。