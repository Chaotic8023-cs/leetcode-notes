from typing import *


class Solution:
    """
    回溯：此题和40组合总和2，还有90子集2类似，需要横向去重。但是，此题找的是非递减子序列，也就是说我们不能事先进行排序，否则顺序将被打乱。
    所以，这里我们就不能用prev去记录上一个循环用的是什么，而是用一个统一的set去记录！
    """
    def backtracking(self, state, nums, start_idx, ans):
        if len(state) >= 2:
            ans.append(state[:])
            # 这里不return，因为如果return了结果就只会保存长度为2的，我们记录一个长度为2的还需要继续加！
        used = set()  # 因为不能排序，所以我们用一个统一的set去记录整个for循环使用过的元素（即本层搜索树中横向的分支不能用之前用过的）
        for i in range(start_idx, len(nums)):
            if (len(state) == 0 or nums[i] >= state[-1]) and nums[i] not in used:
                used.add(nums[i])  # 因为是不是纵向去重，所以回溯回来不删除！
                state.append(nums[i])
                self.backtracking(state, nums, i + 1, ans)
                state.pop()


    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtracking([], nums, 0, ans)
        return ans



if __name__ == '__main__':
    sol = Solution()
    nums = [4, 6, 7, 7]
    print(sol.findSubsequences(nums))





