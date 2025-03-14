from typing import *


"""
一直觉得排列的题目很有趣，终于想通了根据当前排列计算出下一个排列的方法，在这里记录一下。 例如 2, 6, 3, 5, 4, 1 这个排列， 
我们想要找到下一个刚好比他大的排列，于是可以从后往前看 我们先看后两位 4, 1 能否组成更大的排列，答案是不可以，同理 5, 4, 1也不可以。
直到3, 5, 4, 1这个排列，因为 3 < 5， 我们可以通过重新排列这一段数字，来得到下一个排列 因为我们需要使得新的排列尽量小，
所以我们从后往前找第一个比3更大的数字，发现是4 然后，我们调换3和4的位置，得到4, 5, 3, 1这个数列 因为我们需要使得新生成的数列尽量小，
于是我们可以对5, 3, 1进行排序，可以发现在这个算法中，我们得到的末尾数字一定是倒序排列的，于是我们只需要把它反转即可。
最终，我们得到了4, 1, 3, 5这个数列 完整的数列则是2, 6, 4, 1, 3, 5。

步骤总结：
1. 从后向前遍历，找到第一个下标i：nums[i] < nums[i + 1]。如果找不到，说明整个数组降序排列，直接翻转即可。
2. 找到i后，再从后向前遍历，找到第一个比nums[i]大的nums[j]，交换ij
3. 最后翻转一开始找到的下标i后面的部分
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first_min_idx = -1  # 要设为-1，因为first_min_idx可能刚好是0，即恰好只有第一个数是最小的，例如[1,4,3,2]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_min_idx =  i
                break
        if first_min_idx == -1:
            nums[:] = nums[::-1]  # 没找到第一个i比i+1小的，说明整个数组是降序排列的，已经是最大排列了，所以按题目要求直接反转，返回最小的排列即可
            return
        # 找到了第一个i比i+1小的，此时i的后面从左往右一定是降序排列，我们在i的右边找到第一个比i大的数和i进行交换，即从后向前遍历第一个比i大的就是要和i交换的数
        for i in range(n - 1, first_min_idx, -1):
            if nums[i] > nums[first_min_idx]:
                nums[first_min_idx], nums[i] = nums[i], nums[first_min_idx]
                break
        # i后面本来就是降序排列，把小一点的i交换到第一个比i大的地方后，还是降序。因为下一个排列我们要尽可能小，所以把i后面的降序序列翻转一下即可
        nums[first_min_idx + 1:] = nums[first_min_idx + 1:][::-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    sol.nextPermutation(nums)


