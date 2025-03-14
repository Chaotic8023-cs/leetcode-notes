from typing import *


class Solution:
    """
    双循环+双指针：思路同三数之和（1循环+双指针），这里我们加一个循环，即双循环+双指针。记的时候可以不记剪枝!
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for i in range(n):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:  # i去重
                continue
            for j in range(i + 1, n):
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:  # j去重：注意，j的最小值是i+1，所以跟前面比的时候j-1也得最小值为i+1
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        # left和right去重
                        left, right = left + 1, right - 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
        return ans

    """
    有剪枝版本
    
    需要注意的时四数之和中的剪枝和三数字和不一样了，因为target不是0了，例如：
    [-4, -1, 0, 0], target = -5，i=-4 > target，但我们不能把-4排除！
    所以剪枝的时候需要数组元素和target都>0的情况才能排除！

    还需注意的时第二个剪枝不能直接返回最后的答案（只有第一个剪枝可以），因为剪枝只是在前面已经确定的数字固定后，
    在寻找后面几个数的时候可以停止查找。这里我们看i+j > target后，只是在i固定后，当前的j（和34两个数）没必要往后找了，
    但是下一轮有不同的i时，j还可能和i相加小于target（如i=1， j非常大比如5时和i相加大于target了，那么下一轮中i=2时，虽然变大了，
    但是j是从3开始找的，所以i+j还是可能小于target的！）。
    """
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:  # 一级剪枝（可省略）
                break
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] > target and target > 0:  # 二级剪枝（可省略）
                    break
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left, right = left + 1, right - 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
        return ans




