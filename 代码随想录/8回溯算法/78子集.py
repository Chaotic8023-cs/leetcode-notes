from typing import *


class Solution:
    """
    回溯：其实子集就是所有可能的组合，就像下面自己写的那样。但是其实通过观察搜索树，我们发现其实所有可能的组合就是一个没有长度限制的组合问题，即把k去掉，
    然后我们要的答案不仅是叶节点，中间即跟节点也是答案，即我们把is_goal检查去掉，收集所有包括中间的结果就是子集。要注意的是和组合一样，只能
    选当前选过的后面的数字以防止重复的组合
    """
    def backtracking(self, state, nums, start_index, ans):
        ans.append(state[:])  # 收集所有结果，包括中间（即去掉组合中的长度等于k的检查）
        for i in range(start_index, len(nums)):  # start_index指当前开始选的位置
            state.append(nums[i])
            self.backtracking(state, nums, i + 1, ans)
            state.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtracking([], nums, 0, ans)
        return ans


class Solution1:
    """
    回溯：自己写的，思路：子集其实就是在求所有可能的组合组合，即先求n选0，n选1，一直到n选n，用index求。在求出所有组合后再用index从原数组中提取即可。
    """
    def get_next_comb(self, state, n, k):
        if len(state) == 0:
            return list(range(n))
        return list(range(state[-1] + 1, n))

    def backtracking_comb(self, state, n, k, ans):
        if len(state) == k:
            ans.append(state[:])
            return
        for x in self.get_next_comb(state, n, k):
            state.append(x)
            self.backtracking_comb(state, n, k, ans)
            state.pop()

    def combination(self, n, k):
        ans = []
        self.backtracking_comb([], n, k, ans)
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        # 用index的所有可能的组合从原数组提取子集
        for i in range(n + 1):  # 即n选i
            combinations = self.combination(n, i)
            for comb in combinations:
                ans.append([nums[k] for k in comb])
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))



