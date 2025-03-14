# 202
from typing import *


class Solution:
    # 若n为happy number，则最终会变为1
    # 若n不是happy number，则会陷入循环，但会recurrent，即在过程中会出现重复!
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            x = 0
            while n:
                n, rem = divmod(n, 10)  # quotient, remainder = divmod(x, y)
                x += rem ** 2
            n = x
        return n == 1

    # 快慢指针找链表环
    # https://zhuanlan.zhihu.com/p/454262200
    # 解法2:
    # O(1) space. 如果无空间限制，则可以用hashmap, 每次插入value，直到变成1 (happy)，或者遇到重复(not happy)
    """
    It can be proved that if n is not a happy number, It will finally goto a
    4→16→37→58→89→145→42→20→4 loop.
    所以我们用快慢指针，快指针每次走两步，慢的一步
    若是happy number，两个指针都会变成1循环，即两个指针相遇（变成1后）后value是1
    若不是happy number，则整个链表可看作有上述loop的一个存在循环的链表，
    则快指针一定会和慢指针相遇，且相遇时value不是1
    
    (因为快指针每次走两步，慢指针一步，即快指针每次比慢指针多走一步，即快慢指针间的距离每次缩短1，所以
    快指针一定会追上慢指针且不会有越过的情况。如果快指针每次比慢指针多走>1步的话，即可能出现越过的情况，但还是会相遇
    一般我们都用快2慢1的方法)
    """

    def isHappy1(self, n: int) -> bool:
        def next(x):
            y = 0
            while x:
                x, r = divmod(x, 10)
                y += r ** 2
            return y

        # 应该同时从n出发，但为了while循环条件，让fast比slow一开始就先多一步，不影响
        # (相当于都先走了一步，fast比slow快1步，接下来就是快2步，3步...)
        slow, fast = n, next(n)
        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return slow == 1


if __name__ == '__main__':
    n = 19
    sol = Solution()
    print(sol.isHappy(n))
