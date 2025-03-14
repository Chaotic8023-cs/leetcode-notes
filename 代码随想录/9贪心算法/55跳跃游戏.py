from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max_range = nums[0]
        for i in range(1, len(nums)):
            if i <= curr_max_range:
                curr_max_range = max(curr_max_range, i + nums[i])
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))


