# 35
from typing import *


class Solution:
    """
    第1种：（统一记这种！）
    Invariant：target insert position一直在[l, r)中
    所以当mid大于target时，我们应该在左半部分[l, r-1]继续找，但我们更新r=mid，因为Invariant中右边为开区间
    loop condition为l < r，即当l==r时结束，因为在在[l, r)中当l==r时search space才变空
    Initialize: 同样符合Invariant，即l=0满足左闭，r=len(nums)满足右开

    第2种：
    Invariant：target insert position一直在 [l, r]中
    所以当mid大于target时，我们更新r=mid-1，因为Invariant中右边为闭区间
    loop condition为l <= r，即当l > r时结束，因为在在[l, r]中当l > r时search space才变空
    Initialize: 同样符合Invariant，即l=0满足左闭，r=len(nums)-1满足右闭

    注意，我们记第一种即可：
    1. 当target存在于nums里时，loop停的条件是l==r，所以在停之前的最后一个循环中，l和r挨着，也就是说else一定会被执行，
    所以意味着此时target严格大于mid。因为l和r挨着，算出的mid=l，所以l此时指向target的左边1位，r指向target，此时满足
    target严格大于mid（也就是l），最终l会被更新+1，指向target。这里其实找到的是leftmost的target如果有重复，在这里插入新的一个同样的
    target不会破坏nums的顺序。
    2. 当target不存在于nums里是，同理，结束前的最后一个loop中，l和r会挨着，然后else会被执行使得l==r。也就是说，此时target严格大于mid，
    即l指向的是小于target的第一个元素，r指向的是大于target的第一个元素，此时mid是l，target严格大于mid，最后l会+1和r重合，也就是说l最后
    指向大于target的第一个元素，就是insert的位置！

    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:  # nums[mid] < target
                l = mid + 1
        return l

    def searchInsert1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l