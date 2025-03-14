from collections import deque
from typing import *


class Solution:
    """
    stack：匹配括号是用stack解决的经典问题，我们遍历括号字符串，如果是开括号就加入到stack中，
    当遇到闭括号则从stack中pop出一个开括号看能不能和当前的比括号匹配上。逻辑是当遇到闭括号时，它
    一定要和最近的那个括号匹配，stack中存开括号的顺序刚好满足了LIFO顺序，即刚才进入的最后一个开括号。
    在检查过程中如果stack变空了（没有与当前闭括号对应的开括号了）或pop出来的开括号与当前的闭括号无法对应，则直接返回False。
    要注意的时最后我们需要检查stack是否为空，如果空了则说明都匹配完了，如果不为空，则说明有stack中多余的开括号没有与之对应的闭括号，
    需要返回False
    """
    def isValid(self, s: str) -> bool:
        stack = deque()  # 存开括号
        open = set("([{")
        close = set(")]}")
        pairing = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p in open:
                stack.append(p)
            if p in close:
                if not stack or stack.pop() != pairing[p]:
                    return False
        return len(stack) == 0

