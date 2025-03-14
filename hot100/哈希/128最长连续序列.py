from typing import *


"""
用一个set（哈希表）记录所有元素以便快速查找。我们遍历数组，我们想要找到可能的连续序列起点，所以如果num - 1存在就跳过；当找到序列的起点时，
就一直把当前的序列从set中移除，并统计当前递增序列的长度。
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in s:  # 当前num不是递增序列的起点，跳过
                continue
            # 计算以num为起点的递增序列的长度
            curr = num
            while curr in s:
                s.remove(curr)  # 同时去除当前序列中的元素
                curr += 1
            ans = max(ans, curr - num)
        return ans





if __name__ == '__main__':
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums))


