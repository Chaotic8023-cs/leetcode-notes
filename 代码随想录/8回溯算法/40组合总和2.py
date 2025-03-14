from typing import *


class Solution:
    """
    回溯（有重复元素，需要横向去重）：此题是组合的和中最难的一道，因为候选集中可以有重复的元素。这里我们就舍弃了模板中的is_goal和get_next，而是把它们直接写到
    backtracking中以获得更细的控制。

    例如[1,1,2]，target = 3。我们会发现第1个1和第2个1加上2结果都为3，那么我们需要去重（注意，如果候选集中有多个相同的数字，它们是可以
    被选多次的，只要不超过它出现的总数即可）。也就是说在搜索树中，在一个分支中纵向是不用去重的，即后面没用过的，即使是重复出现，也能使用。但是，
    横向看，即分支和分支之间需要去重：在例子中，第一个1经过回溯后得到的答案一定包含了以第2个1为开头的所有答案，所以我们需要在回溯结束后进行
    横向去重。

    具体实现就是记录上一个pop掉的元素（注意，是回溯后，这样回溯中就不会去重，在后半部分的即使是重复也能使用），在pop掉这个元素后，如果下一个
    要加入的元素和上次pop掉的一样，则跳过。例如在上面的例子中，最外层的递归的for循环就是全部candidates[1,1,2]，在第1个1递归完成后，
    以1开头的所有答案就会被找齐，当我们loop到第二个1时，和前面pop掉的一样，那我们直接跳过即可。

    注意的是，这样的横向去重逻辑是需要先把候选集先排序的，因为每次比较是跟上一次pop掉的进行的！
    """
    def backtracking(self, state, candidates, target, ans, start_idx):
        s = sum(state)
        if s == target:
            ans.append(state[:])
            return
        elif s > target:
            return

        prev = None  # 记录上一个递归的入口元素，这样比较确保了深度搜索（即递归backtracking的调用）中不去重，而是横向去重
        # start_idx记录我们当前可以选的元素的位置
        for i in range(start_idx, len(candidates)):  # for循环是广度搜索（横向，需要去重），backtracking()是纵向搜索，不需要去重
            if candidates[i] == prev:  # 如果当前元素和上一个递归的入口元素一样则跳过
                continue
            state.append(candidates[i])
            self.backtracking(state, candidates, target, ans, i + 1)
            prev = state.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)  # 事先进行排序，以配合横向去重
        self.backtracking([], candidates, target, ans, 0)
        return ans


if __name__ == '__main__':
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(sol.combinationSum2(candidates, target))
