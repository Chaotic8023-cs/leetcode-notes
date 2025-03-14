# 45
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        curr_max = nums[0]
        prev_max = nums[0]
        prev_max_start = 0
        curr_max_start = 0
        """
        MyVer
        dp[i]表示到i需要最多的跳跃次数

        curr_max: 当前能达到的最远位置
        prev_max: 前一次能达到的最远位置
        prev_max_start: 前一次能达最远位置的起始点
        curr_max_start: 当前一次能达最远位置的起始点
        每次到i时，我们看从prev_max_start能不能到当前位置，
        如果可以则一直从prev_max_start跳一步，即 dp[i] = dp[prev_max_start] + 1
        如果超出了前一次能达到的最远位置，我们则从curr_max_start跳到当前位置，
        并更新prev_max = curr_max和prev_max_start = curr_max_start

        即贪心思想：只要当前的位置i包含在前一次max里，则当前位置就从前一次的start跳过来
        """
        for i in range(1, n):
            if i <= prev_max:
                dp[i] = dp[prev_max_start] + 1
            else:
                dp[i] = dp[curr_max_start] + 1
                prev_max = curr_max
                prev_max_start = curr_max_start
            if (m := i + nums[i]) > curr_max:
                curr_max = m
                curr_max_start = i
        return dp[n - 1]

    def jump1(self, nums: List[int]) -> int:
        ans = mx = last = 0
        """
        AnsVer
        每次到i就先记录mx：当前等跳到的最远的位置
        我们用last记录上一次跳跃到的位置，即我们assume
        每次跳跃，都“提前”跳到当前能跳的最远位置 (初始时相当于上次跳到了index 0)。
        如果当前的i到了上一次的跳跃到的位置，即last==i，那么
        我们就再跳一步（更新ans），但是相当于是从当前能跳到最远位置的start（即mx更新时的index）
        跳了那么多，因为上次跳到的位置（即当前位置）一定包含这个start
        我们只需要loop到倒数第二个位置即可，因为我们是每次“提前跳跃”，
        当到倒数第二个位置是，我们判断是否上次跳跃的结尾是这，如果不是说明已经跳到末尾了（倒数第一个index）
        则无需多跳一步！
        这个思想和上面自己写的其实原理一样
        """
        for i, x in enumerate(nums[:-1]):
            mx = max(mx, i + x)
            if last == i:
                ans += 1
                last = mx
        return ans


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    print(sol.jump1(nums))
