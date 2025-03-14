# https://kamacoder.com/problempage.php?pid=1191
"""
拓扑排序：给出一个有向图，把这个有向图转成线性的排序就叫拓扑排序。
当然拓扑排序也要检测这个有向图是否有环，即存在循环依赖的情况，因为这种情况是不能做线性排序的。所以拓扑排序也是图论中判断有向无环图的常用方法。

步骤：
    重复：
    1. 找到入度为0 的节点，加入结果集
    2. 将该节点从图中移除
    如果找不到入度为0的节点且还有剩余节点，则证明图中有环，不能做线性排序了
"""
from collections import defaultdict, deque


def main():
    # 读数据
    n, m = map(int, input().split())
    graph = defaultdict(list)  # 用于记录依赖关系，用map的话方便直接读取每个节点都指向谁
    in_degree = [0] * n
    for _ in range(m):
        s, t = map(int, input().split())
        graph[s].append(t)  # s -> t：t依赖于s
        in_degree[t] += 1
    # 解题
    q = deque([i for i in range(n) if in_degree[i] == 0])  # 初始化队列：加入一开始入度为0的节点，即从无依赖的节点开始
    ans = []
    while q:
        curr = q.popleft()
        ans.append(curr)
        # "删除"当前节点：graph不用动，只需要根据graph来更新in_degree即可
        for t in graph[curr]:
            in_degree[t] -= 1
            if in_degree[t] == 0:  # 把新的入度为0的加入队列
                q.append(t)
    # 打印结果
    if len(ans) == n:
        print(" ".join(map(str, ans)))
    else:  # 还有剩余节点，说明有环，无法排序
        print(-1)


if __name__ == '__main__':
    main()
