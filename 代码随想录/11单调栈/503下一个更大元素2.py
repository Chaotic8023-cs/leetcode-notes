from collections import deque
from typing import *


class Solution:
    """
    就是496下一个更大元素1改成了循环数组。我们直接拼接一个一样的数组到后面然后过一遍单调递增栈即可。
    如果不想复制一遍数组，还可以用求余的方法处理index。
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mStack = deque()
        n = len(nums)
        arr = nums + nums  # 其实可以不用复制以便数组，直接用%即可算超出数组的index（如n = 3， 那么i = 4就相当于4 % 3 = 1）
        ans = [-1] * 2 * n
        for i in range(2 * n):
            while mStack and arr[i] > arr[mStack[-1]]:
                prev_i = mStack.pop()
                ans[prev_i] = arr[i]
            mStack.append(i)
        return ans[:n]

class Solution1:
    """
    也可以使用wrap index：mstack中存两倍nums的下标，即[0, 2n - 1]，记录的时候对n求余即可
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mstack = deque()  # 记录下标
        ans = [-1] * n  # ans只用记录前n个，因为我们一直对i求余
        for i in range(2 * n):
            while mstack and nums[i % n] > nums[mstack[-1] % n]:
                prev_i = mstack.pop()
                ans[prev_i % n] = nums[i % n]
            mstack.append(i)
        return ans

    """
    当然，ans也可以初始化成2n长度的，然后仅在访问nums时求余，记录到ans中时仍使用2倍的下标
    """
    def nextGreaterElements1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mstack = deque()
        ans = [-1] * 2 * n  # 记录2倍nums的下标
        for i in range(2 * n):
            while mstack and nums[i % n] > nums[mstack[-1] % n]:
                prev_i = mstack.pop()
                ans[prev_i] = nums[i % n]  # 直接记录长度为2倍nums的下标
            mstack.append(i)
        return ans[:n]  # 最后只取前n个



