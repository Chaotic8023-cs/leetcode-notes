# https://programmercarl.com/kamacoder/0053.%E5%AF%BB%E5%AE%9D-Kruskal.html

"""
Kruskal总结：每次选权重最小且加入后不会有环的边，加入到当前的最小生成树中
"""
class Edge:
    def __init__(self, i, j, w):
        self.i = i
        self.j = j
        self.w = w  # weight

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


def kruskal(v, e, edges):
    ds = DisjointSet(v + 1)  # 适应 1-indexed（节点从1开始）所以用v+1
    sum_weights = 0
    mst_edges = []
    # 对edge进行排序
    edges.sort(key=lambda edge: edge.w)
    for edge in edges:
        pi, pj = ds.find(edge.i), ds.find(edge.j)
        if pi != pj:
            ds.union(pi, pj)  # 已经call过一次find了，所以直接union parent即可
            sum_weights += edge.w  # 加上当前要加入的边的权重
            mst_edges.append((edge.i, edge.j))  # 记录当前加入到生成树的边
    return sum_weights, mst_edges


def main():
    # 读取数据
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        i, j, w = map(int, input().split())
        # kruskal只记录所有边即可
        edges.append(Edge(i, j, w))

    # 解题
    sum_weights, mst_edges = kruskal(v, e, edges)
    # 打印答案
    print(sum_weights)
    # 扩展：打印所有边。kruskal因为直接操作的是边，所以记录的就是按顺序加入的边
    # print(mst_edges)



if __name__ == '__main__':
    main()





