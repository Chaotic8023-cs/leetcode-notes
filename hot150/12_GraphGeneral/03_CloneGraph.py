# 133
from typing import *
from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # 简单递归解法
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        原理同self try，这里visited其实既充当了visited set又充当了hashtable
        直接递归clone，每次populate neighbours前检查当前node是否已经复制过了，
        没复制过就新复制一个并populate它的neighbors，复制过就直接返回visited里的
        这样就保证了对于原始graph中每个node都单独复制一次并populate了它的neighbour，
        且不会陷入无限循环
        """
        visited = defaultdict()  # key是原始的node，value是新复制的node

        def clone(node):
            if node is None:
                return None
            if node in visited:
                # 如果复制过了直接用复制过的，这个同时保证了复制过的node不会再遍历它的neighbors，防止了无穷递归
                return visited[node]
            # 对于每个没复制过的node，复制它并populate它的neighbors
            new_node = Node(node.val)
            visited[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(clone(n))
            return new_node

        return clone(node)

    # self try
    def cloneGraph1(self, node: Optional['Node']) -> Optional['Node']:
        """
        我们用dfs遍历原始graph里的node，用visited防止重复
        用一个哈希表new_nodes来记录创建的新的节点（用node.val作key）
        每次遍历到原始graph中的一个node，看它是否已经复制过，即查表，
        没复制过就创建个新的记录到表中，复制过就直接用表里的
        然后我们填充这个node的neighbours，同样的我们需要根据原始node的neighbours看是否已经复制过
        即我们用new_nodes保证每个每个node仅复制一次，如果复制过了我们直接用表里的指针
        """
        visited = set()
        new_nodes = {}
        if not node:
            return None

        def dfs(node):
            # visit every node in the graph once to populate its neighbors
            if node.val not in visited:
                visited.add(node.val)
                # if this node already copied (in the hashtable, then use the previous copied one)
                if node.val not in new_nodes:
                    n = Node(node.val)
                    new_nodes[node.val] = n
                else:
                    n = new_nodes[node.val]
                # populate the neighbors of this node, if already copied the use the pointer in the hashtable
                for neighbor in node.neighbors:
                    if neighbor.val in new_nodes:
                        n.neighbors.append(new_nodes[neighbor.val])
                    else:
                        new_neighbour = Node(neighbor.val)
                        new_nodes[new_neighbour.val] = new_neighbour
                        n.neighbors.append(new_neighbour)
                # visit other nodes in the graph once each
                for neighbor in node.neighbors:
                    dfs(neighbor)

        dfs(node)
        return new_nodes[1]  # 返回第一个节点，即val=1的


if __name__ == '__main__':
    sol = Solution()
