# 33
from typing import *

# [1,2,3,4,5,6,7]
# [2,3,4,5,6,7,1]
# [3,4,5,6,7,1,2]
# [4,5,6,7,1,2,3]
# [5,6,7,1,2,3,4]
# [6,7,1,2,3,4,5]
# [7,1,2,3,4,5,6]
class Solution:
    # 二分查找
    def search(self, nums: List[int], target: int) -> int:
        """
        每次找mid，把array分成2部分[0:mid]和[mid+1:]，两个中一定有一个是递增的：
        如何判断那部分是有序数组：比价array[0]和array[mid]，如果mid比array[0]大，
        则说明[0:mid]是有序数组，反之则是[mid+1:]。注意，这里要用nums[0] <= nums[mid]，用=是因为
        当left right挨在一起时(即left为nums[0]，right为nums[1])，mid就是left，这时mid就等于nums[0]，
        同样满足条件！

        1. 如果[0:mid]是有序数组：
            1> 如果target在[0:mid]，则我们可缩小搜索范围，就在[0:mid]继续找
            2> 否则，在后半部分[mid+1:]中继续找
        2. 如果[mid+1:]是有序数组：
            1> 如果target在[mid+1:]，则我们可缩小搜索范围，就在[mid+1:]继续找
            2> 否则，在前半部分[0:mid]中继续找
        终止条件为left == right，我们看最终看此时的两个指针是否为target

        注意，分成两部分不能有重叠！即[0, mid]，第二部分一定是[mid+1:]！
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            # 此时target不是mid，那么一定在左右两侧
            if nums[0] <= nums[mid]:  # [0, mid]递增
                if nums[0] <= target < nums[mid]:  # 在mid左边：用mid比，此时target一定不等于mid了
                    right = mid
                else:  # 在mid右边
                    left = mid + 1
            else:  # [mid + 1:]递增
                if nums[mid] < target <= nums[-1]:  # 在mid右边：还是用mid比，不用mid+1是因为边界条件下mid+1会超出有效下标的范围!
                    left = mid + 1
                else:
                    right = mid  # 在mid左边
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([3, 1], 0))
