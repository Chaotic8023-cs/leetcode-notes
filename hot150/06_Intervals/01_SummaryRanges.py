# 228
from typing import *


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        start = nums[0]
        acc = start
        for i in range(1, len(nums)):
            num = nums[i]
            if num == acc + 1:
                acc = num
            else:
                res.append(f"{start}->{acc}" if acc > start else f"{start}")
                # reset start and acc
                start = num
                acc = start
        # append to ensure unsaved changes are write to result
        res.append(f"{start}->{acc}" if acc > start else f"{start}")
        return res

    # sol2: Two Pointer
    def summaryRanges1(self, nums: List[int]) -> List[str]:
        def f(start: int, end: int) -> str:
            return f"{start}->{end}" if end > start else f"{start}"
        res = []
        start = 0  # starting index
        while start < len(nums):
            # for each start, find consecutive nums until end index
            end = start
            while end+1 < len(nums) and nums[end+1] == nums[end]+1:
                end += 1
            res.append(f(nums[start], nums[end]))
            # move to next index
            start = end+1
        return res


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    sol = Solution()
    print(sol.summaryRanges1(nums))
