from typing import *


class Solution:
    """
    贪心：分治，每次只考虑一边的约束，即先考虑左比右大，再考虑右比左大，最后再合起来（取max）去满足both
    """
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lr = [1] * n
        rl = [1] * n
        # 只考虑左比右大，最右边的孩子为起始值为1，因为大的要比小的分更多的糖果，所以为了保证能累加，应该从小的往大的遍历，所以从右往左遍历
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                lr[i] = lr[i + 1] + 1
        # 只考虑右比左大，最左边的孩子起始值为1，从左向右遍历
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                rl[i] = rl[i - 1] + 1
        # 为了同时满足左比右大和右比左大的条件，我们取max即可
        return sum([max(x, y) for x, y in zip(lr, rl)])

    """
    贪心自己写的：按rating从小到大分糖果，这样总数就最小的
    """
    def candy1(self, ratings: List[int]) -> int:
        n = len(ratings)
        # 对原数组进行排序(不改变位置，只获得按排序顺序的原始下标)，因为可能有重复rating，所以先按值排再按原来数组的index排
        sorted_indices = sorted(enumerate(ratings), key=lambda x: (x[1], x[0]))  # 排序好的 (原始index,value)
        candys = [-1] * n
        for idx, (i, rating) in enumerate(sorted_indices):  # 按从小到大的rating分配糖果
            lcandy = candys[i - 1] if i - 1 >= 0 else -1
            rcandy = candys[i + 1] if i + 1 < n else -1
            lrating = ratings[i - 1] if i - 1 >= 0 else float('inf')
            rrating = ratings[i + 1] if i + 1 < n else float('inf')
            if idx == 0:  # 第一个小孩分1个
                candys[i] = 1
            elif rating > lrating and ratings[i] > rrating:  # 比两边都大，则分两边最多的那个+1
                candys[i] = max(1, lcandy, rcandy) + 1
            # 比一边大，则分比小的那边多1
            elif rating > lrating:
                candys[i] = max(1, lcandy) + 1
            elif rating > rrating:
                candys[i] = max(1, rcandy) + 1
            # 默认分1
            else:
                candys[i] = 1
        return sum(candys)






if __name__ == '__main__':
    sol = Solution()
    ratings = [1,2,87,87,87,2,1]
    print(sol.candy(ratings))












