# https://kamacoder.com/problempage.php?pid=1179

"""
并查集：将所有边加入DS，最后src是否能到dest就相当于：src和dest是否属于同一个set，即有相同的parent
"""
class DisjoinSet:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return True
        self.parent[pb] = pa


def main():
    n, m = map(int, input().split())
    ds = DisjoinSet(n + 1)
    for _ in range(m):
        s, t = map(int, input().split())
        ds.union(s, t)
    src, dest = map(int, input().split())
    # src和dest如果在一个set中，则说明src能到dest
    if ds.find(src) == ds.find(dest):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()

