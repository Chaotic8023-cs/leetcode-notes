from typing import *
from math import floor, sqrt



"""
我们可以发现，对于一个灯泡，开关奇数次则亮着，偶数次则关着。
同时，根据开关规律，可以发现第i个灯泡开关次数等于其因数个数：
1: 1
2: 1, 2
3: 1, 3
4: 1, 2, 4
5: 1, 5
6: 1, 2, 3, 6
7: 1, 7
8: 1, 2, 4, 8
9: 1, 3, 9
...

通过观察发现，被开关奇数次的灯泡都是完全平方数，例如1、4、9，
所以题目就转化为求小于等于n的完全平方数个数，
答案记住就行：根号n向下取整
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return floor(sqrt(n))