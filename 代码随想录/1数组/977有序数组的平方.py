from typing import *


class Solution:
    """
    思路：双指针法，因为可能有负数，所以两头的平方一定是最大的，我们用两个指针从两头往里遍历，从大往小的加
    i，j从两头往中间走，往ans加的顺序是从大到小
    这个方法也适用于全为正或全为负的，在这种情况就只有一个指针动
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        ans = []
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):  # 每次先加大的，因为两头（或其中的一头）最大
                ans.append(nums[i] ** 2)
                i += 1
            else:
                ans.append(nums[j] ** 2)
                j -= 1
        return ans[::-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.sortedSquares(nums))


