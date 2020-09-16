class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.subJudge(nums)

    def subJudge(self, nums: List[int]) -> bool:  # 当nums长度为1且数值为24时返回True
        if len(nums) == 1:
            return bool(abs(nums[0] - 24) < 0.000001)
        flag = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                tmp = nums.copy()
                tmp.remove(nums[i])
                tmp.remove(nums[j])
                new_num = [a + b, a * b, a - b, b - a]
                if a != 0:
                    new_num += [b / a]
                if b != 0:
                    new_num += [a / b]
                for new in new_num:
                    # print([each] + tmp)
                    flag += self.subJudge([new] + tmp)
        return bool(flag)

