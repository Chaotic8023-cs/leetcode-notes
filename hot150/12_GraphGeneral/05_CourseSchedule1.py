# 207
from typing import *
from collections import defaultdict


class Solution:
    """
    Topological Sort (Kahn's Algorithm, not for traditional array sorting): find a topological order in a DAG

    Lemmas:
        1. If G is a DAG, then G has a node with no entering edges.
        2. If G is a DAG, then G has a topological ordering.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        问题可以基于DAG做，课程0是课程1的前置课，则可以看作一个edge：0 -> 1
        于是问题可以被转换成在建立的graph中是否又cycle，即存在两个或多个课互相为前置
        我们使用Kahn's Algorithm去找topological order，如果又topological order即意味着G没有cycle
        Kahn's Algorithm大致如下：
        建立graph G，初始化一个set S记录incoming edge数为0的的nodes，初始化count(w)记录所有nodes 的incoming edges的数量
        每次从S中remove掉一个node n，并从graph中删除这个node n（因为n没有incoming，所以只有outgoing， 所以可以直接
        从adjacency list中删除它，即删除它的outgoing edges）
        同时，我们更新count(w)，即对于每个n的outgoing edge w，count(w) -= 1，然后如果w的incoming edge变为0了，即count(w)=0，那么
        把node w也加入到S中
        最后S为空时，如果graph中nodes已经删完了，则说明topological order找到了，即G中无cycle
        如果G中还有nodes，则说明无法找到topological order，即G中有cycle
        """
        g = {i: [] for i in range(numCourses)}  # graph in adjacency list
        zero_in_degree_nodes = []  # set representing the nodes that has 0 in-degree: no ingoing edges
        in_degree_count = defaultdict(lambda: 0)
        # topological_order = []  # a valid topological order is the order to take courses
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
            # topological_order.append(n)
            # remove the node in the graph (no need)
            # for each edge n->w, decrement in-degree of w, if in-degree of w == 0, add w to zero_in_degree_nodes
            for w in g[n]:  # decrement in-degree counts
                in_degree_count[w] -= 1
                if in_degree_count[w] == 0:
                    zero_in_degree_nodes.append(w)
        # when set of 0-degree nodes become empty, if no remaining nodes in the graph (我们用count，所以不用真正
        # 从G remove nodes), then a topological order is found, otherwise, there exists a cycle in the graph
        # print(topological_order)
        return ct == numCourses


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0], [0, 1]]
    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))


