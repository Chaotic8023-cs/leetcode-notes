# 11
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def get_area(start, end):
            return (end-start) * min(height[end], height[start])
        """
        Greedy+双指针：
        一开始start，end指向两头，不妨假设左边的柱子矮，这时候宽度最大，能盛的水就是由
        矮的start决定的。这时如果将end左移，不管end变高还是变矮，盛的水一定会减少。所以
        我们每次移动矮的那个，直到start和end相遇
        """
        start, end = 0, len(height)-1
        curr_max = get_area(start, end)
        while start < end:
            curr_max = max(curr_max,get_area(start, end) )
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return curr_max


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    print(sol.maxArea(height))

