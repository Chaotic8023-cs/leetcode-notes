from typing import *
from collections import defaultdict
# https://programmercarl.com/kamacoder/0109.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5II.html


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
            return True
        self.parent[pv] = pu
        return False


class Solution:
    """
    节点的入度+并查集找环：在有向树中，每一个节点只有一个父节点，所以除了root的入度为0外其余每个节点的入度都为1。
    既然多一条边，那么就有可能有一个节点的入度为2。所以我们就统计所有节点的入度，然后找出入度为2的节点对应的两个边。我们找的时候
    按edge从后往前找入度为2的节点，就可以满足多重答案选靠后的。要注意的是有些情况只有一条边可以去除，所以要检查去除后还是不是树，如果
    不是则去除两条边中的另一条（优先靠后，不行就去除靠前的那条）。第三种情况就是没有入度为2的节点，但有环，我们就去用
    并查集找到并去除形成环的那那条边即可。
    """
    def find_cycle_edge(self, edges):  # 用并查集找到形成环的那条边
        n = len(edges)
        ds = DisjointSet(n + 1)  # +1因为节点从1开始，相当于下标0我们就不用了
        for u, v in edges:
            if ds.union(u, v):
                return [u, v]

    def is_tree_after_delete(self, edges, edge_to_remove_idx):  # 检查删除一条指定的边后是否为树
        n = len(edges)
        ds = DisjointSet(n + 1)  # +1因为节点从1开始，相当于下标0我们就不用了
        for i in range(n):
            if i == edge_to_remove_idx:  # 跳过要删除的边
                continue
            if ds.union(edges[i][0], edges[i][1]):  # 如果有环则不是树
                return False
        return True

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # 因为多一条边，所以边 == 节点
        # 统计所有节点入度
        in_degree = defaultdict(int)
        for u, v in edges:
            in_degree[v] += 1
        # 在edges中从后往前找入度为2的那个节点对应的那两条边
        in_degree_2 = []  # 存放入度为2的那个节点对应的两条边在edges中的下标
        for i in range(n - 1, -1, -1):  # 从后向前遍历edges来找入度为2的节点（即u->v中的v）因为题目中要求如果有多个答案则给出靠后的答案
            u, v = edges[i]
            if in_degree[v] == 2:  # 当前edge指向的节点的入度为2，记录当前边的下标（某个节点入度为2，所以一共会记录两个边）
                in_degree_2.append(i)
        # 分情况讨论：一共两种种情况(因为有向树中每个节点只有一个父节点，所以多一条边就可能造成入度为2的节点，我们按有无入度为2的节点分类讨论)
        if in_degree_2:  # 有入度为2的节点（此时in_degree_2记录的是那个节点对应的两条边）
            # 情况1.1：有1个节点的入度为2，对应两条边，我们删除其中靠后的那个（即先记录的下标0），看删除后是否为tree
            if self.is_tree_after_delete(edges, in_degree_2[0]):
                return edges[in_degree_2[0]]
            # 情况1.2：有1个节点的入度为2，对应两条边，但只能删除靠前的那个，因为删除靠后的那个结果不是树
            else:
                return edges[in_degree_2[1]]
        # 情况2：没有入度为2的节点，图中有环，找出形成环的那条边即可（天然的会返回最后一个，因为构建并查集时一旦形成环了自然就是最后一条边）
        else:
            return self.find_cycle_edge(edges)








