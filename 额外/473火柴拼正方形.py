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



