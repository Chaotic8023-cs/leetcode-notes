from typing import *


"""
类似518零钱兑换2：此题和它一模一样，只是换成求排列了。在求排列的完全背包问题中，先遍历背包，后遍历物品！
2d直接调换两个循环行不通，也不知道为啥，即只有求组的时候先物品后背包行得通，所以直接记1d的就行！
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1  # 求方法数则dp[0] = 1
        # 遍历：求排列则反过来遍历，先背包后物品！
        for j in range(target + 1):  # 背包容量：因为在外层，所以从0开始遍历，下面手动检查是否当前背包容量放不下当前物品！
            for i in range(n):  # 物品
                # 2d这里应当是dp[i][j] = dp[i - 1][j]，1d中这里就是dp[j] = dp[j]，所以可以直接省略
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]  # 求方法数则选i和不选i加起来，背包+爬楼梯！
        return dp[target]



if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    target = 4
    print(sol.combinationSum4(nums, target))