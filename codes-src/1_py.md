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
Runtime: 3972 ms
Memory Usage: 13.9 MB
时间空间效率都属于低段。
