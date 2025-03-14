# 219
from typing import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}  # key: num, value: index
        for idx, num in enumerate(nums):
            # 如果遇到重复，只需把index更新到当前的index即可
            # 不需要存遇到的这个num的所有index，因为是顺序遍历
            # 要index距离小于等于k，只需和前面最近遇到的相同num进行比较即可！
            if num in hm:
                if abs(idx-hm[num]) <= k:
                    return True
            hm[num] = idx
        return False


if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
