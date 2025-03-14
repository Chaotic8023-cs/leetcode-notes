from typing import *


class Solution:
    """
    贪心：删除最少的区间使得不重叠其实就是求重叠区间的个数。我们先按start排序好判断区间是否重叠。我们一次只看两个区间，如果有重叠则删除
    其中一个。贪心就体现在删除两个中的哪个：因为我们要尽可能的使之后的重叠变少（所以总删除数就会少），且我们判断重叠是按下一个start和当前
    的end进行比较，所以我们选则留下end更小的那个，即删除end更偏右的那个。在代码的体现中我们就每次把end更新成更偏左的（min）那个，即
    我们删掉end更大的那个区间。因为l是排序过的，所以只用考虑r就可以看是否有重叠了。
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        ans = 0
        i = 0
        while i < n:
            l, r = intervals[i]
            i += 1
            while i < n and intervals[i][0] < r:  # start < r：有重叠
                r = min(r, intervals[i][1])  # 隐式删除：通过取min来删除两个重叠区间右边界大的那个，所以留下的就是end小的那个
                i += 1
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    print(sol.eraseOverlapIntervals(intervals))





