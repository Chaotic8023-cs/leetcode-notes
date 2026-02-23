from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_max = 0
        i = 0
        while i <= curr_max:
            curr_max = max(curr_max, i + nums[i])
            if curr_max >= n - 1:
                return True
            i += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))


