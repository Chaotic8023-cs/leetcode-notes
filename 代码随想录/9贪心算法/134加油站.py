from typing import *


class Solution:
    """
    贪心思路：其实我们看的就是油量的delta，即我们到每站所能获得的汽油净增量。如果能走完一圈，那么我们累计的油量一直都是>=0的，所以根据这个
    我们遍历diff，如果在第i站时当前的累计油量小于0了，说明i之前的所有位置出发都不能走完一圈，此时清零累计油量从i+1起步继续。我们同时记录
    sum(diff)，最后的时候如果sum(diff)小于0说明从哪出发都不能走完一圈。
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]  # 汽油的净增量delta
        # 看diff的总和是否为负，如果为负说明从哪走都走不了一圈（因为走完一圈一定每个地方都走到了，所以diff求和一定>=0）！
        if sum(diff) < 0:
            return -1
        curr_sum = 0
        ans = 0  # 默认从下标0出发（如果从0真的能走一圈，则for里面的if就不会跑，curr_sum会一直 >= 0）
        for i in range(n):
            curr_sum += diff[i]
            if curr_sum < 0:
                ans = i + 1
                curr_sum = 0
        return ans

    """
    暴力解法：从每个能出发的起点都模拟一边
    """
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        def canGo(start, n):
            curr = start
            remaining = gas[curr] - cost[curr]
            curr = (start + 1) % n
            while curr != start and remaining >= 0:
                remaining += gas[curr] - cost[curr]
                curr = (curr + 1) % n
            return True if curr == start and remaining >= 0 else False

        n = len(gas)
        for i in range(n):
            if cost[i] > gas[i]:  # 当前i不能出发，跳过
                continue
            if canGo(i, n):
                return i
        return -1

