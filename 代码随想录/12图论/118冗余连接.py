from typing import *
# https://programmercarl.com/kamacoder/0108.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5.html


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
        if pu == pv:  # 要加入的边两头的节点uv已经在一个set里了，即此边会形成环
            return False
        self.parent[pv] = pu
        return True  # union成功

class Solution:
    """
    并查集：利用union来判断是否为冗余边：如果要加入的边两头的节点uv已经在一个set里了，则此边会形成环，即冗余边
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet(len(edges) + 1)  # 因为图中多一条边，所以节点数就是len(edges)，+1因为节点从1开始，下标0相当于不用了
        for u, v in edges:
            if not ds.union(u, v):  # 如果union失败，即此边形成环，则为冗余边
                return [u, v]











