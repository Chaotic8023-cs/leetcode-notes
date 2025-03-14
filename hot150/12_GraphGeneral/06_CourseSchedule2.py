# 210
from typing import *
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        和#207一样，只是这题需要返回上课的顺序，即topological order
        """
        g = {i: [] for i in range(numCourses)}  # graph in adjacency list
        zero_in_degree_nodes = []  # set representing the nodes that has 0 in-degree: no ingoing edges
        in_degree_count = defaultdict(lambda: 0)
        topological_order = []  # a valid topological order is the order to take courses
        # populating g, initial 0 in-degree nodes
        for c, pre in prerequisites:
            g[pre].append(c)
            in_degree_count[c] += 1
        for i in range(numCourses):
            if in_degree_count[i] == 0:
                zero_in_degree_nodes.append(i)
        ct = 0  # count, use to track the num nodes removed (so no need to actually remove nodes from G)
        while zero_in_degree_nodes:
            n = zero_in_degree_nodes.pop()
            ct += 1
            topological_order.append(n)
            # remove the node in the graph (no need)
            # for each edge n->w, decrement in-degree of w, if in-degree of w == 0, add w to zero_in_degree_nodes
            for w in g[n]:  # decrement in-degree counts
                in_degree_count[w] -= 1
                if in_degree_count[w] == 0:
                    zero_in_degree_nodes.append(w)
        # when set of 0-degree nodes become empty, if no remaining nodes in the graph (我们用count，所以不用真正
        # 从G remove nodes), then a topological order is found, otherwise, there exists a cycle in the graph
        return topological_order if ct == numCourses else []


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    sol = Solution()
    print(sol.findOrder(numCourses, prerequisites))


