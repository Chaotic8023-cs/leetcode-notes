from collections import deque
from typing import *

"""
单调递减队列（从队首到队尾单调递减）：队首一直存当前窗口的最大值，窗口每次滑动后要加入一个元素v前，先把队尾所有小于v的元素pop掉来保证单调性；窗口
每次滑动后要去除前一个窗口的第一个元素，单调队列中pop元素v时当且仅当v是队首最大的那个元素。
"""
class MonotonicQ:
    def __init__(self):
        self.q = deque()

    def append(self, v):
        while self.q and self.q[-1] < v:  # 在append前把队尾所有小于v的元素都去掉！
            self.q.pop()
        self.q.append(v)

    def get_max(self):
        return self.q[0]

    def popleft(self, v):
        if self.q and self.q[0] == v:
            return self.q.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = MonotonicQ()
        n = len(nums)
        for i in range(k - 1):  # 先加入前k - 1个
            mq.append(nums[i])
        ans = []
        # 每次补全当前窗口最后一个，然后get_max，最后去掉当前窗口第一个
        for i in range(k - 1, n):
            mq.append(nums[i])
            ans.append(mq.get_max())
            mq.popleft(nums[i - k + 1])
        return ans







