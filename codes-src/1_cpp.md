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
Runtime: 436 ms 属于最慢的
Memory Usage: 9.3 MB 击败99.07%
额。。时间最慢，空间最快。。
基本可以推测出，还有一种主流的做法是正好相反：时间快，空间大的。
估计是STL中的另一个数据结构。