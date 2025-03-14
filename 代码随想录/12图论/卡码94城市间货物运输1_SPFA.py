# https://programmercarl.com/kamacoder/0094.%E5%9F%8E%E5%B8%82%E9%97%B4%E8%B4%A7%E7%89%A9%E8%BF%90%E8%BE%93I-SPFA.html
from collections import deque
"""
SPFA (Shortest Path Faster Algorithm)：即队列优化版的Bellman Ford。可以不用记，只用记基础版的即可。
"""


def SPFA(n, m, edges, start, goal):
    minDist = [float('inf')] * (n + 1)
    minDist[start] = 0
    q = deque([start])
    isInQueue = [False] * (n + 1)
    isInQueue[start] = True
    parent = [-1] * (n + 1)
    while q:
        i = q.popleft()
        """
        我们每次只松弛从上一次松弛过的节点出发的边：我们是先松弛ij再把j加入q，下一次我们松弛j出发的边，
        所以下一次只需要松弛j，就不用重复加入j了，所以引入一个isInQueue，只需要确保当前松弛完i出发的所有
        节点j后，j都在queue里即可，如果j已经在了就不用重复加入
        """
        isInQueue[i] = False
        for j, w in edges[i]:
            if minDist[i] != float('inf') and minDist[i] + w < minDist[j]:
                minDist[j] = minDist[i] + w
                parent[j] = i
                if not isInQueue[j]:
                    q.append(j)
                    isInQueue[j] = True

    # 此时不能再松弛了，即结束了
    if minDist[goal] != float('inf'):
        return minDist[goal], reconstruct_path(parent, start, goal)
    else:
        return None, None


def reconstruct_path(parent, start, goal):
    curr = goal
    path = []
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]
    if path[0] == start:
        return path
    return None



def main():
    # 读取数据
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]  # 用邻接表，因为SPFA中要快速获得一个节点所有的连接
    for _ in range(m):
        i, j, w = map(int, input().split())
        edges[i].append((j, w))
    # 解题
    cost, path = SPFA(n, m, edges, 1, n)
    # 打印答案
    if cost is not None:
        print(cost)
        # print(path)
    else:
        print("unconnected")



if __name__ == '__main__':
    main()





