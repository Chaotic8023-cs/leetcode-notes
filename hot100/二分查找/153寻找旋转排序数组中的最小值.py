from typing import *


"""
记忆：处理数组为旋转的特殊情况后，每次mid和nums[0]比较：
    1. nums[0] <= nums[mid]: [0, mid]单增，最小值一定在mid右边 -> left = mid + 1
    2. nums[0] > nums[mid]: [mid + 1:]单增，最小值一定在mid + 1左边 -> right = mid
最后和普通二分一样return nums[left]

注意：其实mid还可以每次和nums[right]进行比较，就可以省去处理数组为旋转的特殊情况，但是那样写法很怪，不符合一直记的左闭右开，所以不记那个。
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 处理特殊情况：数组未旋转
        if nums[0] <= nums[-1]:  # 有=因为有可能数组只有一个元素
            return nums[0]
        # 二分搜索：统一左闭右开
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:  # [0:mid]单增，所以最小值一定在mid的右边
                left = mid + 1
            else:  # [mid + 1:]单增，所以最小值一定在mid + 1的左边（这里看似right = mid会把mid排除在外，但最后一次循环中一定走的是left = mid + 1，即还会找到mid如果mid就是最小值！）
                right = mid
        return nums[left]


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 4, 5, 6, 1]
    print(sol.findMin(nums))
