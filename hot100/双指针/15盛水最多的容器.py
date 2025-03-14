from typing import *


class Solution:
    """
    双指针：ij分别指向两头，每次计算完容量后移动矮的那个指针
    """
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            ans = max(ans, (j - i) * min(height[i], height[j]))  # 计算当前容量
            # 移动矮的那个指针
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans





