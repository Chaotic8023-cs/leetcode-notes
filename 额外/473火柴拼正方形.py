from typing import *


"""
第一想法必然是枚举所有可能，即回溯，但是实现上：
1. 枚举方法：不用纪录每根火柴属于哪个边，只需要记录四条边当前的长度就行！
2. 剪枝：否则会超时！
    - 提前算一下每条边的长度（cap），回溯中过滤掉超出当前边长度的情况
    - 按火柴长度先倒排一下，这样可以提早过滤掉后续超出cap的情况
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def backtracking(state, idx, cap):
            if idx == len(matchsticks):
                # 这里直接return True就行，因为所有火柴都用完了，且都没超出cap，即一定满足条件！
                return True
            # 枚举：当前火柴可能在4条边中的任意一边
            for i in range(4):
                if state[i] + matchsticks[idx] <= cap:  # 当前边能放下
                    state[i] += matchsticks[idx]
                    if backtracking(state, idx + 1, cap):
                        return True
                    state[i] -= matchsticks[idx]
            return False
        
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        cap = s // 4
        state = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)  # 重要：倒排，这样大火柴在前，可以提早过滤掉一些超出cap的情况！不倒排的话会超时！
        return backtracking(state, 0, cap)


# 状压dp + 记忆化搜索解法，参考 https://www.bilibili.com/video/BV15a4y1o7NA
class Solution1:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(nums, status, cap, curr, rest, dp):
            """
            状压dp + 记忆化搜索：dfs表示在当前状态下，能否（最终）凑出正方形
            
            nums: matchsticks
            status: 以二进制表示每个火柴是否可用，1表示可用，0表示不可用（已经用过了）
            cap: 正方形的边长，用作选边的限制
            curr: 当前边累积的长度
            rest: 剩余几条边需要凑
            dp: 记忆化搜索，防止某个status被重复计算。
                dp[0]表示没被计算过，1和-1分别表示True和False
            """
            if rest == 0:  # base case：拼成了正方形
                return True  # 因为我们是按规矩凑的，所以所有4条边凑完后，一定合法
            if dp[status] != 0:  # cache命中
                return dp[status] == 1
            ans = False
            for i in range(len(nums)):
                # 当前火柴能选：需要第i位为1，用&判断。注意条件是!=0而不是==1，因为在i>0的情况下&过后的值是2^i
                if status & (1 << i) != 0 and curr + nums[i] <= cap:
                    if curr + nums[i] == cap:  # 当前边恰好拼好了
                        ans = dfs(nums, status ^ (1 << i), cap, 0, rest - 1, dp)
                    else:  # 当前边还没凑完
                        ans = dfs(nums, status ^ (1 << i), cap, curr + nums[i], rest, dp)
                    # 如果拼好了则停止继续递归
                    if ans:
                        break
            dp[status] = 1 if ans else -1  # 记住结果共后续复用
            return ans

        n = len(matchsticks)
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        cap = s // 4
        # dp：status共n位，每位01两种可能，所以需要2^n的空间
        dp = [0] * (1 << n)
        # status初始化：假设4根火柴，则应该表示为1111，即先1 << 4 = 10000，再减1变成1111
        return dfs(matchsticks, (1 << n) - 1, cap, 0, 4, dp)