# 55
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        """
            贪心：
            max_jump记录当前能跳到的最远index，遍历nums，
            如果当前的index比max_jump大，说明我们无法跳到当前
            index，直接return False，因为当前的到不了后面就也到不了了！
            如果能到，则更新max_jump，当前位置能跳到最远的位置就是i+nums[i]
            """
        max_jump = 0
        for i in range(n):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
        return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    print(sol.canJump(nums))
