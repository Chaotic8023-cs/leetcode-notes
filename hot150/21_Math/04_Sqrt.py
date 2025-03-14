# 69
from typing import *


class Solution:
    """
    Naive中我们一个一个试会超时，所以用二分查找法:
    我们用左开右闭的形式
    当mid * mid > x，target一定在左边，但为什么我们这里用mid-1，使得mid-1取不到呢？
    因为我们想要找的是向下取整，即最后一个target^2小于x的数，
    这个二分法当left == right停止，也就是走right = mid - 1这个if
    在最后一个循环中，left和right一定挨在一起，例如3和4
    我们要找的其实是3，即3^2恰好小于x同时4^2恰好大于x
    所以我们直接更新right = mid - 1来使得right往左移最后等于left
    要注意的是我们需要修改mid的计算方法，即计算mid时我们+1，这样在最后一个循环中mid就是右边那个数，例如3和4中的4，即right，
    这样mid^2会大于x从而走if而不是else（会陷入死循环，因为计算mid不+1的话mid此时是left）
    """
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left