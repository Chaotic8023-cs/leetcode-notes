from typing import *
from math import inf


class Solution:
    """
    贪心：因为利润最大，所以买入那天一定是卖出那天之前的一个最小值。维护一个目前的最小值，然后假设每天卖出，在每天更新ans(当天价格减去
    到当天为止所遇到所有价格中的最小值)即可。
    """
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = inf  # 当前的最小值
        ans = 0
        for p in prices:
            if p < curr_min:
                curr_min = p
            ans = max(ans, p - curr_min)  # 每个价格减去目前遇到的所有价格中的最小值就是当天卖出所能获得的最大利润
        return ans



