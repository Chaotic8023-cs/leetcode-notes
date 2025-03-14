from typing import *


"""
动态规划：
直接跟着力扣题目上的动图做就行，dp数组直接就是结果。
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * (i + 1) for i in range(numRows)]  # 初始化：第n行arr大小就是n，我们用0-index
        for i in range(2, numRows):  # 从第3行开始，因为前两行初始化的时候就已经填满1了
            for j in range(1, i):  # 遍历当前row的中间部分，即去掉头尾
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # 左上和右上，看图就知道左上的下标是j-1，右上和当前下标一样是j
        return dp






