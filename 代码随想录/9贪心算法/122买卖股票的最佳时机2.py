from typing import *


class Solution:
    """
    双指针+贪心：获得最大利润其实就是找递增的区间，也就是说在每个递增区间开头买入，末尾卖出，即获利最大。找单增区间用快慢指针即可。
    """
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        n = len(prices)
        ans = 0
        while j < n:
            while j < n and prices[j] >= prices[j - 1]:  # 找当前递增区间，注意包含=，因为价格不变也算在一个递增区间内
                j += 1
            ans += prices[j - 1] - prices[i]
            i = j  # 下一个递增区间的开头买入
            j += 1
        return ans

    """
    简化版：求递增区间的利润和就是把每两天的利润为正的累加起来
    """
    def maxProfit1(self, prices: List[int]) -> int:
        p = [prices[i] - prices[i - 1] for i in range(1, len(prices))]  # 每两天的利润
        return sum([i for i in p if i > 0])  # 只要正利润


if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))



