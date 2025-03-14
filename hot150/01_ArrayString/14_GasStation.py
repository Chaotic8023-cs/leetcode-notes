# 134
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_sum = 0
        total_sum = 0
        start = 0
        """
        贪心：
        我们看每次的净增油量，即在i处加了gas[i]的油再消耗cost[i]的油之后的油量：
        idx:     0, 1, 2, 3, 4
        gas:    [2, 5, 2, 3, 5]
        cost:   [1, 2, 8, 2, 4]
        diff:    1  3 -6  1  1
        
        我们用一个current_sum来记录当前的累计增量（累计diff），total_sum来记录从头
        到尾的总体累计增量。如果遍历一遍之后total_sum为负，则无论从哪出发都无法走一
        圈（因为无论从哪走走一圈累计都是total_sum）！
        对于current_sum，在遍历到i时如果变为负数，则表明到不了i+1了：说明从上次起点到
        i之间这个区间内任何位置出发都不能走完一圈（因为到i了增量就为负了）。
        我们可能会想如果是从这个区间内某个点出发到i会不会增量为正呢？答案是不会：
        [start       r1       |        r2       i]
        假设我们从start开始（current_sum=0）一直累加到i发现净增变成负数了，则说明
            sum(r1) + sum(r2) < 0
        假设从中间（｜）处出发到i净增为正数的话，则说明
            sum(r2) > 0
        ->  sum(r1) < 0
        我们就会发现如果从中间某处出发到i净增大于0的话，我们在中间的时候净增就已经小于0了，
        与一开始到i净增才为0矛盾。所以只要遇到净增为负，我们就只能从下一个index出发！
        """
        for i in range(len(gas)):
            gain = gas[i]-cost[i]  # 净增
            # total_sum和current_sum用一个for记录就省去了单独算一遍total_sum！
            current_sum += gain    # 当前累计净增
            total_sum += gain      # 总共累计净增
            if current_sum < 0:
                # 从0到i出发都不可能走完一圈！
                start = i+1        # 设i+1为起点
                current_sum = 0    # 重置当前累计净增
        if total_sum < 0:
            # total_sum < 0 -> 无论任何起点都走不完一圈
            return -1
        return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))



