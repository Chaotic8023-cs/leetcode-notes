from typing import *


"""
子集是全组合问题，即不考虑顺序，123和321算一种，后面选的时候就不能往前面再选了，所以用start_idx记录当前选的起始位置，每次只能从起始位置开始选。
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start_idx, state, ans, nums):
            # 根本不需要检查超出边界：当start_idx == len(nums)时，刚好选完了，这时候ans会append一下结果，但for循环就不会跑，相当于自动return了（省去写if start_idx > len(nums): return）
            ans.append(state[:])  # 因为是所有子集，每次都是valid结果，都要append
            for i in range(start_idx, len(nums)):
                state.append(nums[i])
                backtracking(i + 1, state, ans, nums)
                state.pop()

        ans = []
        backtracking(0, [], ans, nums)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))



