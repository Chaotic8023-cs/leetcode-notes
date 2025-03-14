from collections import deque
from typing import *


"""
单调队列：始终保持元素大到小排列（单调递减），队列的头部始终是当前滑动窗口的最大值。

思路：我们用一个单调递减的队列去维护当前窗口的值，但是保持当前窗口的最大值一定在头部，即队列里的元素单调递减。
每次加入元素之前，如果队列末尾的比要加入的小，则一直从尾部pop掉，直到加入这个新元素后单调递减性质能保持为止（q[-1] >= v即可）

例子：[1, 4, 2, 3], k = 3
第一个窗口[1, 4, 2]:
    1. 加入1：[1]
    2. 加入4：此时队列的末尾1比4小，则先从尾部pop掉，再加入4：[4]。可以理解为当前窗口中1比4小了，所以1不可能是最大值，我们就不需要维护它了。
    3. 加入2：2比队列末尾的4小，满足单调递减性质，所以可以直接加入：[4, 2]
    最后调用getMax()，即获取队列头部的元素4，即为当前窗口的最大值。
第二个窗口[4, 2, 3]:
    1. 首先我们要pop掉第二个窗口的前一个元素1，但是1在之前已经pop了。实际上的逻辑是我们拿要移除的元素和队列的头进行比较，如果相等才popleft。
    2. 加入新元素3：当前队列为[4, 2]，末尾元素比3小，所以先pop掉2变成[4]，此时满足条件了再加入3，最后为[4, 3]。
    最后调用getMax()，即获取队列头部的元素4，即为当前窗口的最大值。
"""
class MonotonicQueue:
    def __init__(self):
        self.mq = deque()

    def append(self, v):
        while self.mq and self.mq[-1] < v:
            self.mq.pop()  # 加入新元素前把q末尾所有小于v的元素都删除（注意，这里是pop不是popleft，即从末尾删除！）
        self.mq.append(v)

    def pop(self, v):
        if self.mq and self.mq[0] == v:
            return self.mq.popleft()

    def get_max(self):
        return self.mq[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = MonotonicQueue()
        n = len(nums)
        # 先加入前k个元素，获取第一个窗口中的最大值
        for i in range(k):
            mq.append(nums[i])
        ans = [mq.get_max()]
        # 再从第二个窗口遍历到到最后一个（遍历滑动窗口的末尾下标）
        for i in range(k, n):
            mq.pop(nums[i - k])  # 删掉前一个窗口的起始位置的元素
            mq.append(nums[i])  # 加入窗口滑动后应该加入的元素（即当前窗口的末尾元素）
            ans.append(mq.get_max())
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))



