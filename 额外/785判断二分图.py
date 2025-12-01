from typing import *


class DisjointSet:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, a):
        if self.parent[a] == -1:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        self.parent[pb] = pa
        return True


"""
解法：并查集
重点是思路中的推导

思路：最终要求所有边的两头节点处于不同的集合 -> 对于一个节点u，其邻居节点都应在同一个集合中，且u不在该集合中。

1. 初始化并查集ds。
2. 遍历graph，对每一个u，将它的所有邻接顶点v都合并起来。
4. 再次遍历graph，对每一个u，考察是否有find(u) == find(v)，满足则graph不是二分图。

实际上无需完整遍历两次，而是把第三步放在第二步的循环中一起做。一旦发现union邻居后u和某个v在同一个set，就可以立即返回false。
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        ds = DisjointSet(n)
        for u, vs in enumerate(graph):
            # 邻居应当在一个set中 -> union所有邻居
            for i in range(len(vs) - 1):
                ds.union(vs[i], vs[i + 1])
            # 一条边的两头是不同set -> 检查u是否和所有邻居处于不同set
            for v in vs:
                if ds.find(u) == ds.find(v):
                    return False
        return True





