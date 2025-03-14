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
