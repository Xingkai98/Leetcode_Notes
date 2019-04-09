### 1
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = 0
        #choose the first one
        for inxi, i in enumerate(nums):
            #clear the list for a new round
            res = []
            
            res.append(inxi)
            t = target - i
            
            #choose the second one 
            for inxj, j in enumerate(nums[inxi+1:]):
                if t == j:
                    
                    #add on inxi + 1 to offset relative index
                    res.append(inxj + inxi + 1)
                    return res
```
#### 数据
Runtime: 3972 ms<br/>Memory Usage: 13.9 MB<br/>时间空间效率都属于低段。<br/>时间复杂度O(n^2)，因为是两个for循环。

#
### 2
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for inxi, i in enumerate(nums):
            if target-i in nums[inxi+1:]:
                return [inxi, nums[inxi+1:].index(target-i) + inxi + 1]
```
#### 数据
Runtime: 892 ms, faster than 35.02%<br/>Memory Usage: 13.9 MB, less than 21.61%<br/>可以看到，**时间**有所改善，空间使用无任何变化。那么变化在哪里呢？<br/>1中是两个for循环，并且res不断被赋值、append和清空<br/>2是一个for循环加一个if，直到return中才建立并返回list。

[back](../notes-src/1.md)
