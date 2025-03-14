from typing import *


class Solution:
    """
    题目中说会无限循环，即会出现重复的和，例如下面的n=2，当算到n=145的时候和前面的42重复了，导致42 - 145这一段一直重复，所以是无限循环
    4, 16, 20, 37, 42, 58, 89, 145 (1^2 + 4^2 + 5^2 = 42, duplicate)
    所以我们只需一个set来记录，如果和出现过了则return False，否则当n==1时return True
    """
    def isHappy(self, n: int) -> bool:
        def get_sum(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            return s

        record = set()
        while n != 1:
            n = get_sum(n)
            if n in record:
                return False
            record.add(n)
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(2))


