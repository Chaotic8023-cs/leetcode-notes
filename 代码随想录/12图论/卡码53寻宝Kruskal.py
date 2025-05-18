import heapq
# https://programmercarl.com/kamacoder/0053.%E5%AF%BB%E5%AE%9D-Kruskal.html

"""
Kruskal总结：每次选权重最小且加入后不会有环的边，加入到当前的最小生成树中
"""
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
            return False  # 已经在一个set，union失败
        self.parent[pv] = pu
        return True  # union成功


"""
使用排序
"""
def kruskal(edges, v, e):
    ds = DisjointSet(v + 1)  # 适应 1-indexed（节点从1开始）所以用v+1
    sum_weights = 0
    mst_edges = []
    # 对edge进行排序
    edges.sort(key=lambda e: e[0])  # 按weight排序
    for w, v1, v2 in edges:
        if ds.union(v1, v2):
            sum_weights += w  # 加上当前要加入的边的权重
            mst_edges.append((v1, v2))  # 记录当前加入到生成树的边
    return sum_weights, mst_edges


"""
使用最小堆
"""
def kruskal1(edges, v, e):
    sum_weights = 0
    mst_edges = []
    ds = DisjointSet(v + 1)
    heapq.heapify(edges)  # 默认按顺序heapify，所以edges三元组中第一个元素是weight
    """
    Kruskal的停止条件是加了 v-1 条边，而不是visited了所有节点！！！
    这里直接用 while edges，等价于上面sort后遍历所有边，因为加入 v-1 条边后，再加的话union就不会成功，所以不用显式检查，当然显式检查效率更高
    """
    while edges:
        w, v1, v2 = heapq.heappop(edges)
        if ds.union(v1, v2):
            sum_weights += w
            mst_edges.append((v1, v2))
    return sum_weights, mst_edges


def main():
    # 读取数据
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        v1, v2, w = map(int, input().split())
        # kruskal只记录所有边即可
        edges.append((w, v1, v2))  # weight, v1, v2

    # 解题
    sum_weights, mst_edges = kruskal(edges, v, e)
    # 打印答案
    print(sum_weights)
    # 扩展：打印所有边。kruskal因为直接操作的是边，所以记录的就是按顺序加入的边
    # print(mst_edges)



if __name__ == '__main__':
    main()





