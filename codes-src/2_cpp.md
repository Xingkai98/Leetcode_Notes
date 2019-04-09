### 1
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //addon 为进位数
        int addon = l1->val + l2->val;
        addon /= 10;
        ListNode* res = new ListNode((l1->val + l2->val)%10);
        ListNode* tmp = res;
        
        //这里注意条件还要加上addon大于0
        //两个数均加到最高位的时候也不一定就是最高位
        while(l1->next || l2->next || addon){
            int raw_add = 0;
            if(l1->next){
                l1 = l1->next;
                raw_add += l1->val;
            }
            if(l2->next){
                l2 = l2->next;
                raw_add += l2->val;
            }
            //这里注意，最后结果必须10以内，所以取余在外边而不是里边
            //tmp->next = new ListNode(raw_add%10 + addon);
            int real_add = raw_add + addon;
            tmp->next = new ListNode(real_add % 10);
            addon = real_add / 10;
            tmp = tmp->next;
        }
        return res;
    }
};
```
#### 数据
Runtime: 28 ms, faster than 98.43%<br/>Memory Usage: 10.4 MB, less than 99.27%

莫名这次第一次就写到了几乎最优的情况


[back](../notes-src/2.md)
