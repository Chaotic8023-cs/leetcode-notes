from collections import deque
from typing import *


"""
单调递减栈：
思路：对于每个矩形，我们以它的高为标准看最大的矩形面积，即我们需要找到它左右两边第一个比它矮的矩形。所以我们用单调递减栈，如果遇到当前的高度
小于栈顶，则栈顶的右侧第一个更小的就是当前元素；左边第一个更矮的就是它弹出后栈顶的元素。要注意的是左右两边如果没有更小的，则下标分别设为有效
下标往外移一格的地方，即-1和len(heights)，这样方便计算宽度。
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mstack = deque()
        ans = 0
        for i in range(n):
            while mstack and heights[i] < heights[mstack[-1]]:
                # 以prev_i的高度为当前高度，找到左右第一个比prev_i小的，即看prev_i的高度最多往两侧延申多少
                mid = mstack.pop()
                h = heights[mid]
                right = i  # 当前的i就是右边第一个比prev_i小的
                left = mstack[-1] if mstack else -1  # 如果mstack有元素，则栈顶就是左边第一个比prev_i小的，因为它是prev_i之前加入的第一个比prev_i小的元素；如果没有元素，那么说明左边没有比prev_i小的，所以就设为第1个矩形的左边，即下标-1
                w = right - left - 1  # 左右两边都比prev_i小，只算中间有效的宽度
                ans = max(ans, h * w)
            mstack.append(i)
        # 此时mstack中剩余的元素就是右边没有比它更小的了
        while mstack:
            mid = mstack.pop()
            h = heights[mid]
            right = n  # 因为右边没有更高的了，所以设为有效下标的最后一位的右边，即len(heights)
            left = mstack[-1] if mstack else -1  # 同理，mstack有元素那么左边第一个比prev_i小的就是栈顶元素，否则设为0下标的左边
            w = right - left - 1
            ans = max(ans, h * w)
        return ans


if __name__ == '__main__':
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(sol.largestRectangleArea(heights))


