from typing import *


class Solution:
    # 和找最左边的target一样，记同一个就行
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + right >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if 0 <= left < len(nums) and nums[left] == target:  # 直接判断left指针在不在有效区间
            return left
        return -1

    # 更efficient的话如果mid就是target直接返回
    def search1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + right >> 1
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 13
    print(sol.search(nums, target))

