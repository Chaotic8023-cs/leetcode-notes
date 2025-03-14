from collections import deque
from typing import *


class Solution:
    """
    单调栈：看了提示后自己做出来的（最初的几次提交没搞对边界情况）。
    此题类似42接雨水，不过这里是找左右两边第一个比当前柱子小的，所以用单调递减栈（从栈顶到栈底单调递减）。
    我们看每个柱子，目标是计算以当前柱子为高的最大矩形面积，所以我们就要找左右两边第一个比当前柱子矮的柱子作为边界。此题重点是边界情况，即两边
    任意一边没有更矮的柱子怎么办。我们每次pop出mid，右边第一个更矮的柱子就是当前遍历到的i，那么左边呢？如果当前mStack中还有元素，说明mid
    之前（mid的左边）加入过比它更矮的柱子（因为单调递减），此时left就是mid弹出后的栈顶元素；如果此时栈是空的，说明mid之前没有比它更矮的了，
    所以mid就是此时最矮的柱子，那我们就把left设为-1，即左边界囊括了mid左边的所有柱子。当遍历完后，如果栈里还剩元素，说明这些元素的右边没有
    比它们更矮的主子了，但我们还需要算它们所构成的最大面积。此时一个一个pop作为mid，right就设为len(heights)，即右边界囊括了mid右边的
    所有柱子（因为此时右边没有比它矮的了）。left和前面的设置方法一样，如果栈里还剩元素，说明mid左边有比它矮的；如果没有，则设置为-1。
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        mStack = deque()
        n = len(heights)
        ans = 0
        for i in range(n):
            while mStack and heights[i] < heights[mStack[-1]]:  # 单调递减栈
                mid = mStack.pop()
                right = i
                left = mStack[-1] if mStack else -1  # 如果栈不空，则说明左边有比mid更矮的；如果栈空，则说明左边没有比mid更矮的了，直接设为-1使得左边界囊括了左边所有的柱子
                h = heights[mid]
                w = right - left - 1
                ans = max(ans, h * w)
            mStack.append(i)
        # 处理栈里剩下的元素，即右边没有比它们更矮的了
        while mStack:
            mid = mStack.pop()
            right = n
            left = mStack[-1] if mStack else -1  # 同理
            h = heights[mid]
            w = right - left - 1
            ans = max(ans, h * w)
        return ans


if __name__ == '__main__':
    sol = Solution()
    heights = [2, 4]
    print(sol.largestRectangleArea(heights))