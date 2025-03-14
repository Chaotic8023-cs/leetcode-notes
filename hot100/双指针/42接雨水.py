from typing import *
from collections import deque


"""
单调递增栈（记录index）：遇到当前元素比栈顶大的就一直弹出：弹出的是mid，当前下标是右边第一个比mid大的，如果栈顶还有元素就是左边第一个比mid大的，
此时就能计算以mid为中间，左右两边为界的一层水的面积
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        mstack = deque()
        n = len(height)
        ans = 0
        for i in range(n):
            while mstack and height[i] > height[mstack[-1]]:
                mid = mstack.pop()
                r = i
                if mstack:
                    l = mstack[-1]
                    h = min(height[l], height[r]) - height[mid]
                    w = r - l - 1
                    ans += h * w
            mstack.append(i)
        return ans




