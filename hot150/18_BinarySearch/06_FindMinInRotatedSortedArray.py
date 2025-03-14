# 153
from typing import *


# [1,2,3,4,5,6,7]
# [2,3,4,5,6,7,1]
# [3,4,5,6,7,1,2]
# [4,5,6,7,1,2,3]
# [5,6,7,1,2,3,4]
# [6,7,1,2,3,4,5]
# [7,1,2,3,4,5,6]


class Solution:
    """
    我们把array每次分成两块：[:mid]和[mid+1:]
    1. 假设array[mid]大于（还有=）arr[0]，则说明[:mid]部分递增，min存在于右半部分[mid+1:]中
    1. 假设array[mid]小于arr[0]，则说明[mid+1:]部分递增，min存在于左半部分[:mid]中（包括mid，因为mid可能就是min）
    """

    def findMin(self, nums: List[int]) -> int:
        """
        当array的第一个比最后一个小的时候，一定没有rotation（或rotate了length(array)次）
        因为如果rotate了，min会在array中间然后开始往后递增，最后再绕回开头，所以rotated array
        开头一定比结尾大！
        """
        if nums[0] < nums[-1]:  # no rotation
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            """
            nums[mid] >= nums[0]有等于号的原因：
            当left right相邻时，比如left=0，right=1，此时如果min在1，mid算出来为0，即left=mid，min在右边，
            所以也应该算作这种情况！
            """
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
        # 最终left=right
        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 4, 5, 6, 7, 1]
    print(sol.findMin(nums))
