from typing import *
# https://kamacoder.com/problempage.php?pid=1179


class DisjointSet:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, u):
        if self.parent[u] < 0:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        self.parent[pv] = pu


class Solution:
    """
    并查集：因为是双向图（即无向图），只要有一条边uv就说明uv在一个集合中，所以直接用并查集即可。
    """
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ds = DisjointSet(n)
        for u, v in edges:
            ds.union(u, v)
        return ds.find(source) == ds.find(destination)  # 如果source和destination在一个集合中即说明u能到达v


if __name__ == '__main__':
    sol = Solution()
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    print(sol.validPath(n, edges, source, destination))





