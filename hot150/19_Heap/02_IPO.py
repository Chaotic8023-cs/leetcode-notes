# 502
from typing import *
import heapq
from collections import Counter
from itertools import count
import random


class Solution:
    """
    双优先队列:
    我们首先把所有project根据花费（capital）加入到q1中
    然后重复k次：
    1. 把q1中所有花费小于当前存款（w）的项目（的利润）加入到q2中，q2按利润的大小倒排，即root是最大的利润（用-profit即可）
    2. q2表示的是当前存款能买的所有project，所以只需选最大利润的那个即可

    注意：此题中买了项目也不会减少当前的capital w，所以简单的greedy：每次选能买的利润最大的project即可
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q1 = [(c, p) for c, p in zip(capital, profits)]  # heapify会按tuple的第一个元素排序
        heapq.heapify(q1)
        q2 = []
        for _ in range(k):
            while q1 and q1[0][0] <= w:
                heapq.heappush(q2, -heapq.heappop(q1)[1])
            if not q2:  # 如果q2为空，即没有项目可以买
                break
            w += -heapq.heappop(q2)
        return w

    # naive: 直接对所有project根据profits和capital进行倒排，每次选能做的最大的那个project -> 超时
    def findMaximizedCapital1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # projects = sorted([(capital[i], profits[i]) for i in range(n)])
        projects = sorted([(profits[i], capital[i]) for i in range(n)], reverse=True)
        for _ in range(k):
            if len(projects) == 0:
                break
            i = 0
            while i < len(projects) and projects[i][1] > w:
                i += 1
            if i == len(projects):  # 所有project都选不了，因为projects中的capital都大于当前的w
                break
            p, c = projects.pop(i)
            w += p
        return w


if __name__ == '__main__':
    sol = Solution()
    k = 1
    w = 0
    profits = [1, 2, 3]
    capital = [1, 1, 2]
    print(sol.findMaximizedCapital(k, w, profits, capital))
