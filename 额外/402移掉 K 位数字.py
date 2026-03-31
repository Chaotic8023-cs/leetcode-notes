from typing import *
from collections import deque


"""
贪心：如果当前数字比前一个数字小，那么前一个更大的数字应该优先删掉。
方法：维护一个单调（递减）栈，如果当前数字比前一个（栈顶）小，则删除栈顶
为什么想到单调栈：栈顶出现在更高位，当前数字更小，用更小的当前数字替代前面更大的数字，一定更优
这就意味着我们希望栈里保持一种趋势，即栈底小，栈顶大，从栈顶到栈底来看就是单调递减栈
    - 如果删完k还大于0，则从末尾删k个（因为此时栈单调递增，即num单增）
    - 最后需要去除前导0
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        mstack = deque()  # 单调递减栈
        for i in range(n):
            # 只要当前数字更小，就尽量删掉前面更大的数字
            # 注意：k必须放到while中，不然k用完了的同时num[i]还小于栈顶就会无穷循环！
            while k > 0 and mstack and int(num[i]) < int(mstack[-1]):
                mstack.pop()
                k -= 1
            mstack.append(num[i])
        ans = ''.join(mstack)
        # 如果还没删够，说明数字整体单调递增，从后面删
        if k > 0:
            ans = ans[:-k]
        # 去掉前导零
        ans = ans.lstrip('0')
        # 最后需要检查是否删完为空，为空则返回0
        return ans if ans else '0'







