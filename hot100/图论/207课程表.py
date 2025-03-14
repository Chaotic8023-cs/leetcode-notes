from collections import defaultdict
from typing import *


"""
判断DAG是否有环：课程c的前置课为pre，那我们构建有向图，其中的edges就是pre -> c。我们用topological sort来找图中是否有环，无环则说明
可以上完。
topological sort：一直删除incoming edges为0的节点。删除一个in-degree = 0的节点后，它所有指向的节点的in-degree都要减1。为了方便
找到某个节点所有的邻居，我们图就选用邻接表。每次删除一个in-degree为0的节点后（不用真从graph中删除，从记录in-degree为0的哈希表中删除即可），
因为它只有outgoing edges，所以它的所有邻居节点的in-degree都要-1。在更新完所有邻居节点的in-degree后，如果为0则加入到哈希表中。一直循环，
直到没有in-degree为0的节点为止。此时如果graph空了，则说明能找到一个topological order，即graph无环。
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}  # 邻接表：pre -> c
        in_degree = defaultdict(int)  # 哈希表，记录所有节点的in-degree
        free = []  # in-dgree为0的节点
        # 创建邻接表
        for c, pre in prerequisites:
            graph[pre].append(c)
            in_degree[c] += 1
        # 收集一开始in-degree为0的节点
        for i in range(numCourses):
            if in_degree[i] == 0:
                free.append(i)
        count = 0
        while free:
            # 删掉一个in-degree为0的节点
            curr = free.pop()  # 把curr记录到一个array中就是topological order
            count += 1
            # 更新它指向的所有节点的in-degree。因为我们有in-degree哈希表来存in-degree为0的节点，所以不需要真正的在graph中删除节点！
            for c in graph[curr]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    free.append(c)
        # 如果graph空了，则说明存在topological order，即不存在环
        return count == numCourses


if __name__ == '__main__':
    sol = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(sol.canFinish(numCourses, prerequisites))

