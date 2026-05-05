from typing import *
from math import *


class Solution:
    """
    核心思路：枚举子矩阵的上下边界，把二维最大子矩阵问题压缩成一维最大子数组问题。

    也就是固定 top 和 bottom 两行后，把这两行之间的每一列加起来，得到一个一维数组 arr。此时，在这个 arr 里找最大连续子数组，就等价于在原矩阵中找一个上下边界固定、左右边界可变的最大子矩阵。

    所以我们需要一个每列的前缀和。
    
    记忆：对于前面0的前缀和，[i,j]的区间和等于psum[j+1] - psum[i]

    重点：一维kadane算法
        其实就是动态规划版最大子数组和的空间优化（滚动数组）。
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        我们发现dp[i]只依赖于dp[i - 1]，所以可以优化掉dp数组了，而用一个变量
        curr_sum代替，即curr_sum = max(curr_sum + nums[i], curr_sum)。
        因为在遍历的是右端点，但是我们需要知道左端点，所以还需要记录left下标。
        何时子数组左端点更新呢？我们发现，当dp[i - 1] < 0时，也就是滚动数组版中curr_sum < 0时，子数组左端点就重置了，即更新为nums[i]，此时记录left = i即可。
    """
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        # 每列的前缀和psum[i][j]: 第j列前i个元素之和
        psum = [[0] * n for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(n):
                psum[i][j] = psum[i - 1][j] + matrix[i - 1][j]
        max_sum = -inf
        ans = [0, 0, 0, 0]  # top, bottom, left, right
        # 枚举top和bottom
        for top in range(m):
            for bottom in range(top, m):
                # 把[top, bottom]之间的行按列压缩成一个一维数组，即col_sum
                arr = [0] * n
                for j in range(n):
                    arr[j] = psum[bottom + 1][j] - psum[top][j]
                # 对arr跑kadane求出最大子数组和，并记录下标
                curr_sum, left = 0, 0
                for i in range(n):  # i是right，需要记录的是left
                    # curr_sum就相当于dp[i]，当dp[i] < dp[i] + nums[i]时，即curr_sum < 0时，子数组左端点重置
                    if curr_sum < 0:
                        curr_sum = arr[i]
                        left = i
                    else:
                        curr_sum += arr[i]
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                        ans = [top, left, bottom, i]
        return ans 







        
