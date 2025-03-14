# 34
from typing import *


class Solution:
    """
    总结：
    使用左开右闭形式：
    target在mid左（arr[mid] >= target）我们往左找（right=mid） ->  leftmost
    target在mid右（arr[mid] <= target）我们往右找（left=mid+1）-> rightmost

    关于为什么leftmost search后left就是leftmost occurrence，但rightmost search后left是rightmost occurrence的右边1位：
    首先我们要知道，loop的最后一个iteration中，left和right会挨着，也就是此时算出的mid=left！
    1. 对于找leftmost，loop的结束条件是left==right，left只有在nums[mid] < target时才被更新，也就是说left想要和right相等，
    只有target严格出现在mid的右边时才会发生。也就是最后一个循环一定是left指向leftmost occurrence的左边1位，
    right指向leftmost occurrence，此时mid算出来会是left，所以target一定比mid大，最后会走else分支，即left+1和right重叠，
    loop结束。所以最终left直接指向的时leftmost occurrence！
    2. 对于rightmost，同理，只有在nums[mid] <= target时left才会+1，也就是说最后一个循环中left指向的是rightmost occurrence，
    right指向的是rightmost occurrence的右边1位，此时mid算出来是left，满足第一个if分支，所以left会+1和right重叠，最终left会处于
    rightmost occurrence的右边1位！

    ！！！为方便记忆，下面两个最后检查left指针时都改成一样的：直接检查最后的位置是否在合理范围内：
        1. leftMost： if 0 <= left < len(nums) and nums[left] == target
        2. rightMost：if 0 <= left-1 < len(nums) and nums[left-1] == target
    怎么记最后的到底是left还是left-1：假定在最后一步更新的都是left = mid + 1，即在最后一个循环中left和right挨着，且mid就是left：
        1. leftMost：此时走left = mid + 1的条件是target严格在mid右边，即target此时在left的右边，也就是right，所以最后更新后
           left刚好就是target
        2. rightMost：此时走left = mid + 1的条件是target >= mid，我们此时认定target就是left，也就是mid，刚好满足这个条件，
           最后left更新完就到target的右边了，所以最后target是left - 1
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftMost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:  # nums[mid] < target
                    left = mid + 1
            if 0 <= left < len(nums) and nums[left] == target:
                return left
            return -1

        def findRightMost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:  # nums[mid] > target
                    right = mid
            """
            loop结束后left会在rightmost的target的右边1位，所以在极端情下，rightmost是nums中最后一个元素，
            那么left就是len(nums), left-1是valid。但是当list为空时，left为0，left-1就是-1了，所以
            只需检查left指针是否是>=0即可
            """
            if 0 <= left-1 < len(nums) and nums[left-1] == target:
                return left-1
            return -1

        return [findLeftMost(nums, target), findRightMost(nums, target)]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    target = 2
    print(sol.searchRange(nums, target))