# https://programmercarl.com/kamacoder/0096.%E5%9F%8E%E5%B8%82%E9%97%B4%E8%B4%A7%E7%89%A9%E8%BF%90%E8%BE%93III.html
"""
特殊Bellman Ford：单源有限最短距离，即最多经过k个城市的最短距离。
注意，经过k个不算起点和终点，例如：1 -> 2 -> 3 -> 4，这里从1开始经过2个城市到达4，即一共k+1=3条边。我们知道普通Bellman Ford中，循环
松弛所有边n次，就能找到与起点n条边相连的节点的最短距离。所以，此题要求最多经过k个城市的最短距离，即循环松弛所有边k+1次即可。

此题reconstruct path比较复杂，可能比较有环，而且出发点不是1，所以就省略了。
"""


def bellman_ford_constraint(n, m, k, edges, start, goal):
    minDist = [float('inf')] * (n + 1)  # 记录目前到所有节点的最短距离
    minDist[start] = 0
    # 所有边松弛k+1次
    for _ in range(k + 1):
        # 重要：因为有限制，所以得做一个minDist的copy，本轮更新只按照上一轮的minDist来算，防止一轮中后面的用前面刚更新过的值！
        prev_minDist = minDist[:]  # prev_minDist记录前一个循环的minDist本循环用前一个循环的数值来做更新
        for i, j, w in edges:
            # 为什么"prev_minDist[i] + w < minDist[j]"中后面用的是最新的minDist的值：因为本轮中可能有多条边到同一个节点，所以用最新的确保本轮这个节点的cost最小！
            if prev_minDist[i] != float('inf') and prev_minDist[i] + w < minDist[j]:
                minDist[j] = prev_minDist[i] + w  # minDist充当当前循环的数值，即最新的数值

    if minDist[goal] != float('inf'):
        return minDist[goal]
    else:
        return None


def main():
    # 读取数据
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        i, j, w = map(int, input().split())
        edges.append((i, j, w))
    src, dest, k = map(int, input().split())
    # 解题
    cost = bellman_ford_constraint(n, m, k, edges, src, dest)
    # 打印答案
    if cost is not None:
        print(cost)
    else:
        print("unreachable")


if __name__ == '__main__':
    main()

