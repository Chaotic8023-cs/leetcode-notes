from math import inf
# https://kamacoder.com/problempage.php?pid=1053

"""
Prim三部曲：
    1. 选距离生成树最近节点
    2. 最近节点加入生成树
    3. 更新非生成树节点到生成树的距离（即更新minDist数组）
"""
def prim(graph, v, e):
    isInTree = [False] * (v + 1)  # 记录当前的生成树，即每个节点是否在树里
    minDist = [inf] * (v + 1)  # 记录每个节点到当前生成树的距离
    parent = [-1] * (v + 1)  # 用来记录最小生成树的（无向）边，此题中用不到，但是如果要打印出所有边就用得上了。parent[i] = j即ij为一条边
    # Prim算法三部曲
    for _ in range(v):  # 每次加入1个节点，一共要加入v个节点
        # 1. 根据minDist选择距离当前生成树最近的一个节点
        curr_node, curr_min = 1, inf  # 因为都用的inf，所以第一次if小于号比较不会成功，所以默认第一个node先加入tree
        for n in range(1, v + 1):
            if not isInTree[n] and minDist[n] < curr_min:
                curr_min = minDist[n]
                curr_node = n
        # 2. 把当前节点curr_node加入当前生成树
        isInTree[curr_node] = True
        # 3. 更新minDist中非生成树节点到当前生成树的距离
        for n in range(1, v + 1):
            # 因为第一次只有一个node，所以第一次更新只有一个节点，之后的更新只要看到新加入的节点的距离是否更小即可！
            if not isInTree[n] and graph[n][curr_node] < minDist[n]:
                minDist[n] = graph[n][curr_node]
                parent[n] = curr_node  # 记录当前的边（注意，因为curr_node固定所以要更新节点n的parent为curr_node，如果用二维邻接矩阵就不用管顺序了，因为一个节点对应全部节点）
    """
    返回：
        1. 最小生成树的边的权重和sum(minDist[2:])：因为minDist数组记录了所有节点到生成树的最小距离，所以从下标2开始就记录了节点2及之后的节点到最小生成树的距离，即边的权重(节点1是第一个加入树的，所以它距树的距离不会更新)
        2. 最小生成树的所有边：通过parent array记录，parent[i] = j即节点i和节点j有连接
    """
    return sum(minDist[2:]), parent

def main():
    # 读取数据
    v, e = map(int, input().split())
    graph = [[float('inf')] * (v + 1) for _ in range(v + 1)]  # 默认节点间距离为无穷
    for _ in range(e):
        i, j, w = map(int, input().split())
        # 无向图所以在邻接矩阵中两个都要赋值
        graph[i][j] = w
        graph[j][i] = w
    # 解题
    sum_weights, parent = prim(graph, v, e)
    # 打印结果
    print(sum_weights)
    # 拓展：打印所有边，parent[i] = j即节点i和节点j有连接
    # for i in range(1, v + 1):
    #     print(f"{i} -> {parent[i]}")


if __name__ == '__main__':
    main()

