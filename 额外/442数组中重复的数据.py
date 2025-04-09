from typing import *


"""
思路同#41缺失的第一个正数，归位数字，然后剩下的就是重复数
时间O(n)，空间O(1)
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        n = len(nums)
        ans = []
        for i in range(n):
            # 当前元素应该放到的位置上（下标nums[i] - 1的元素）不是当前元素时，则交换
            while nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1)
        # 此时所有数字都被归位，那些未归位的就是重复数
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans


"""
方法2:负号标记法
可以理解为，一共有 n 个座位，每个人都要按照车票坐到相应的位置。其中，值为 x 的乘客应该坐在从左往右数第 x 个座位上，也即下标 x−1 处。
1. 一旦这个乘客坐上相应座位，就标记这个位置已经有人坐了；
2. 如果发现要坐的位置被别人占了，就说明有人和你的车票相同，记录答案。

缺点：要求数组中数字严格 > 0，因为使用的是负号标记！
"""
class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            # 因为可能负号标记，所以使用绝对值
            x = abs(nums[i])
            # 座位已经被占，说明当前数重复
            if nums[x - 1] < 0:
                ans.append(x)
            # 标记x对应的座位被占
            nums[x - 1] *= -1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDuplicates(nums))

