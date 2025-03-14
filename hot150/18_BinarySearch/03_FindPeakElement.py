# 162
from typing import *

class Solution:
    """
    二分法：mid和mid+1比较，一直往increase的那半部分找
    因为我们要找其中一个peak，即local maximum，
    同时array中所有数字都不相同，那么我们可以每次看中间的元素，
    然后和它右边的元素进行比较:
        1. arr[mid] < arr[mid+1]
        则local maximum一定存在于[mid+1:]中
        2. arr[mid] > arr[mid+1]
        则local maximum一定存在于[:mid+1]中（包含mid）
    可以这么想，我们每次往increase的方向找，因为数字都不一样，那么这个increase之后一定要么是继续increase要么decrease，所以一定有一个local maximum在这半边存在！
    
    """
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start < end:  # 每次mid和右边的比较，所以条件是start < end，这样剩两个元素的时候mid是start
            mid = (start + end) // 2
            if nums[mid] < nums[mid+1]:
                start = mid+1
            else:
                end = mid
        # 最后return start因为mid小的时候，大的数是start；mid大于的时候，如果mid是最终的peak，则start=end=mid，所以还是start
        return start

    # Linear Search：暴力解法，一个一个位置比较
    def findPeakElement1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if (i-1 < 0 or nums[i] > nums[i-1]) and (i+1 >= len(nums) or nums[i] > nums[i+1]):
                return i

