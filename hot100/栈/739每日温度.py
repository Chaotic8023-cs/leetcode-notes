from collections import deque
from typing import *


"""
单调递增栈（栈顶到栈底单调递增），每遇到比栈顶元素大的，那么它就是栈顶元素右边第一个更大的，此时pop掉栈顶元素并更新栈顶元素的右边更大的温度。
一直重复，直到栈顶不比当前温度小为止。
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        mstack = deque()
        ans = [0] * n
        for i in range(n):
            while mstack and temperatures[i] > temperatures[mstack[-1]]:  # 因为求的是更高的温度，所以是严格大于
                prev_i = mstack.pop()
                ans[prev_i] = i - prev_i
            mstack.append(i)  # mstack存的是小标，因为我们要算天数的差值
        # 最后mstack中剩的小标就是右边没有跟高温度的，ans初始化已经全是0了，所以不用再赋值一遍了
        return ans





