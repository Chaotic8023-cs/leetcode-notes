"""
记忆版本：初始版本+路径压缩
"""
class DisjointSet2:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])  # 路径压缩
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        self.parent[pb] = pa


"""
初始版本
"""
class DisjointSet1:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, a):  # 没有路径压缩会超时！！！
        while self.parent[a] >= 0:
            a = self.parent[a]
        return a

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        self.parent[pb] = pa


"""
优化版本：
    1. find路径压缩
    2. union by size (root的parent存的是-size)
其实union也可以by height。
记的时候就记有路径压缩的初始版本即可。
"""
class DisjointSet2:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])  # 路径压缩
        return self.parent[a]

    def union(self, a, b):  # union by size
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        size_a, size_b = -self.parent[pa], -self.parent[pb]
        if size_a > size_b:
            self.parent[pb] = pa
            self.parent[pa] = -(size_a + size_b)
        else:
            self.parent[pa] = pb
            self.parent[pb] = -(size_a + size_b)



