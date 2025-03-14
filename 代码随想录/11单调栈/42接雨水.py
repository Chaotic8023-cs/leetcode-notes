from collections import deque
from typing import *


class Solution:
    """
    单调栈：每次遇到比栈顶高的，就把栈顶看作mid，当前遍历到的高的就是mid右边第一个比mid高的。为了求水，我们还需要mid左边第一个比mid
    高的。根据单调栈性质，mid在栈顶时，它下面那个元素就是mid之前加进来的（即mid左边），且比mid大，所以它就是mid左边第一个比mid高的。
    此时就可以算：
        1. 高度：min(height[left], height[right]) - height[mid]，即左右两边低的那个减去中间的高度。
        2. 宽度：w = right - left - 1，即以左右两边为界，中间部分的宽度。
    此时以mid为低，left和right为左右两界的中间的这层水的面面积就能算出来。

    这个和暴力解法不同，暴力解法是遍历每个位置，并求出每个位置左右两边最高的柱子（不同于单调栈的第一个高的），此时就能算出当前位置
    的水柱的面积
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        mStack = deque()
        ans = 0
        for i in range(n):
            while mStack and height[i] > height[mStack[-1]]:
                mid = mStack.pop()
                right = i  # 右边第一个比mid大的就是当前遍历到的
                if mStack:  # 栈不为空，即当前的mid左边有比它高的柱子（如果没有说明雨水存不住，就不算了）
                    left = mStack[-1]  # 左边第一个比mid大的就是mid在栈顶时下面的那个元素（在mid之前加入栈，且因为单增比mid大）
                    h = min(height[left], height[right]) - height[mid]
                    w = right - left - 1
                    ans += h * w
            mStack.append(i)
        return ans

    """
    暴力解法：在每个位置i找左右两边的最高的柱子，当前位置的水由左右两边最高的柱子中最低的那个决定。我们在找的时候包括当前位置是
    为了解决当前柱子比左右两边都高的情况（如果不包含最后算出来的water是负数），还解决了其中一边最高的柱子为0的情况（结果同样
    可能是负数），同时还解决了开头和结尾的位置有一边越界的情况。
    """
    def trap1(self, height: List[int]) -> int:
        total_water = 0
        for i in range(len(height)):
            # 算左右最高柱子包含当前位置是为了解决中间柱子最高（或一边没有柱子）的情况，同时也解决了第一和最后一个位置index的问题
            left_max = max(height[0:i+1])
            right_max = max(height[i:])
            water_at_i = min(left_max, right_max) - height[i]
            total_water += water_at_i
            return total_water

