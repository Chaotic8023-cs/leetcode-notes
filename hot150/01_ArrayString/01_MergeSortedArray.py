# 88
from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1  # idx of merged array (m)
        i, j = m - 1, n - 1  # idx for nums1 and nums2, starting from end
        # loop until all nums2 are inserted into nums1, since sorted, remaining nums1 are
        # already sorted!
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
