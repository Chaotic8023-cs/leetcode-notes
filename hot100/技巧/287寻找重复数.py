from typing import *


"""
二分：O(1)额外空间，O(nlogn)时间
原理：因为数字范围是[1, n]，那么对于某个数字x，如果整个数组中 <=x 的数字的个数大于x，则说明数字范围[1,x]中有重复数字，否则[x+1,n]中有重复数字。
例如：[2, 3, 1, 2, 4]，对于数字2，小于等于2的有1,2,2，一共三个，如果2不重复则为1,2两个。此时就说明数字范围[1,2]中出现重复数字了。
所以我们就可以二分搜索，统一左开右闭，数字的范围是[1, n]所以left = 1，right=len(nums)，也就是right = n + 1。注意我们二分是直接分数字[1,n]，
不是下标！
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        while left < right:
            mid = (left + right) >> 1
            count = sum(1 for num in nums if num <= mid)  # 统计 <= mid的数字个数
            if count > mid:  # 数字范围[1, mid]中出现重复
                right = mid
            else:  # count <= mid：数字范围[mid + 1, n]中出现重复
                left = mid + 1
        return left  # 一般都是直接return left，因为最后走的是left = mid + 1，那时候mid为两个挨着的数左边那个，条件为count <= mid，即左边那个数没重复，所以最后就是右边那个数，即left+1后的left


"""
抽屉原理：如果n个东西放到m个抽屉中，n > m，则至少有一个抽屉有>=2个物品
这个是原地解法，会对数组进行改动，不符合题意，但是很巧妙
因为数组长度为n + 1，数字范围是[1, n]，所以所有非重复数字都能放到下标[1, n]上不存在越界问题。
所以我们就把每个数字放到对应的位置上（放到对应的抽屉中），最后如果某个数字要放的对应的抽屉已经放过了，则这个数字就是重复的。

具体实现方法：
下标代表抽屉：放之前（修改nums[i]之前），先把nums[i]的数存下来作为下一个要放的数，然后再标记nums[i] = 0，意味着抽屉i已经放过了。因为数的范围是[1, n]，
所以抽屉0没用，同时我们应该先从nums中第一个数开始，即下标0，所以一开始我们从0开始（虽然一开始给抽屉0存放多余，但是统一了逻辑）。
"""
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            if nums[i] == 0:
                return i
            next_num_to_put = nums[i]  # 修改数nums[i]前记录下一个要放的数
            nums[i] = 0  # 把数字i存放到当前抽屉i
            i = next_num_to_put  # 更新i为下一个要放的数

