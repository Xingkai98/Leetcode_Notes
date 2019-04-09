### 1
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        int target_t = 0;
        //choose the first
        for(auto i = nums.begin(); i != nums.end(); i++){
            res.clear();
            target_t = target - *i;
            res.push_back((int)(i-nums.begin()));
            
            //choose the second
            for(auto j = i+1; j != nums.end(); j++){
                if(*j == target_t){
                    res.push_back((int)(j-nums.begin()));
                    break;
                }
            }
            
            if(res.size() == 2)
                break;
        }
        return res;
    }
};
```
#### 数据
Runtime: 28 ms, faster than 98.43%<br/>Memory Usage: 10.4 MB, less than 99.27%

莫名这次第一次就写到了几乎最优的情况


[back](../notes-src/2.md)
