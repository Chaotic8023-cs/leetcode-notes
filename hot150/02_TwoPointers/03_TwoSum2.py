# 167
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    # 直接binary search
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(nums, n):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if n < nums[mid]:
                    high = mid - 1
                elif n > nums[mid]:
                    low = mid + 1
                else:
                    return mid
            return -1

        for idx, num in enumerate(numbers):
            # 只在后半部分找
            if (k := bin_search(numbers[idx+1:], target-num)) != -1:
                return [idx+1, (idx+k+1)+1]

    # 双指针
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum < target:
                start += 1
            elif curr_sum > target:
                end -= 1
            else:
                return [start+1, end+1]


if __name__ == '__main__':
    numbers = [1,2,3,4,4,9,56,90]
    target = 8
    sol = Solution()
    print(sol.twoSum(numbers, target))

