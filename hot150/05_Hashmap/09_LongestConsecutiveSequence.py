# 128
from typing import *


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    """
    Need to return parent[x], not x!
    if return x, then every recursive find return the input x, 
    which is the parent of caller, not the root!
    if return parent[x], then since the parent along the path gets updated,
    the recursive find will always return the updated parent, which is the root!
    """
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] > self.size[py]:
                self.parent[py] = px
                self.size[px] += self.size[py]
            else:
                self.parent[px] = py
                self.size[py] += self.size[px]

    def insert(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def get_clusters(self):
        clusters = {}
        # k: num, v: parent
        for k, v in self.parent.items():
            root = self.find(v)  # find the root of k
            if root in clusters:
                clusters[root].add(k)  # add the current num to root cluster
            else:
                clusters[root] = {k}  # a set with one element k
        return clusters


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in hm:  # it can be start of a sequence
                n = num+1
                while n in hm:
                    n += 1
                # n is the first num that does not exist,
                # so max length = len([num:n-1]) = n-num
                longest = max(longest, n-num)
        return longest

    # using Union-Find
    def longestConsecutive1(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        ds = UnionFind()
        for num in num_set:
            ds.insert(num)
            # union consecutive nums clusters if exist
            if num-1 in ds.parent:
                ds.union(num, num-1)
            if num+1 in ds.parent:
                ds.union(num, num+1)
            # get the current size of the cluster containing num
            p = ds.find(num)
            size = ds.size[p]
            # update res
            res = max(res, size)
        print(ds.get_clusters())
        return res


if __name__ == '__main__':
    sol = Solution()
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums = [100,4,200,1,3,2]
    print(sol.longestConsecutive1(nums))
