# 209
from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # # Invariant: nums[start:end]一直保存小于target
        start = 0
        current_sum = 0
        n = len(nums)
        min_len = n+1
        for end in range(len(nums)):
            current_sum += nums[end]
            # 对于每个end，一直把start右移来找到最小subarray (sum小于target，即刚好不满足条件)：
            while current_sum >= target:
                # 先更新min_len，即当前满足条件的情况下的subarray的len
                min_len = min(min_len, end-start+1)
                # 再右移start
                current_sum -= nums[start]
                start += 1
        return min_len if min_len <= n else 0


if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))
