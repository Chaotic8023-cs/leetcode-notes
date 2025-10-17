# https://programmercarl.com/kamacoder/0126.%E9%AA%91%E5%A3%AB%E7%9A%84%E6%94%BB%E5%87%BBastar.html
import heapq


"""
注意：heuristic如果选用L1距离的化，不能保证最优路径！
astar给出最优路径的条件是：启发函数h是
    1. admissible: h(n) <= h*(n)
    2. consistent: h(n) <= c(n, n') + h(n')

如果使用L1距离，考虑如下情况：
    A: (0, 0)
    B: (1, 2)
    goal_1: (1, 2)
    goal_2: (2, 3)

    对于goal_1:
    h(A) = |0-1| + |0-2| = 3
    h*(A) = 1
    显然 h(A) <= h*(A)不成立，即h不admissible，不能保证路径最优！

    对于goal_2:
    h(A) = |0-2| + |0-3| = 5
    h(B) = |1-2| + |2-3| = 2
    c(A, B) = 1
    显然 h(A) <= c(A, B) + h(B) -> 5 <= 1 + 2不成立，即h不consistent，不能保证路径最优！
"""
def h(a, b):  # heuristic: 欧拉距离（L2距离）
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

"""
加入q前就检查是否重复
"""
def astar(start, goal, moves):
    q = []
    start_node = (0 + h(start, goal), 0, start, [start])  # (f = g + h, g, node, path)
    heapq.heappush(q, start_node)
    best_g = {start: 0}
    while q:
        f, cost, (x, y), path = heapq.heappop(q)
        if (x, y) == goal:
            return path
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            next_pos = (next_x, next_y)
            next_cost = cost + 1
            if 1 <= next_x <= 1000 and 1 <= next_y <= 1000 and (next_pos not in best_g or next_cost < best_g[next_pos]):  # 在棋盘内，棋盘大小为[1, 1000]
                next_node = (next_cost + h(next_pos, goal), next_cost, next_pos, path + [next_pos])
                heapq.heappush(q, next_node)
    return None

"""
aip课上的写法，从q pop出来才检查有没有重复
"""
def astar1(start, goal, moves):
    q = []
    start = (0 + h(start, goal), 0, start, [start])  # (f = g + h, g, node, path)
    heapq.heappush(q, start)
    best_g = {}
    while q:
        f, cost, (x, y), path = heapq.heappop(q)
        if (x, y) not in best_g or cost < best_g[(x, y)]:
            if (x, y) == goal:
                return path
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                if 1 <= next_x <= 1000 and 1 <= next_y <= 1000:  # 在棋盘内，棋盘大小为[1, 1000]
                    next_pos = (next_x, next_y)
                    next_node = (cost + 1 + h(next_pos, goal), cost + 1, next_pos, path + [next_pos])
                    heapq.heappush(q, next_node)
    return None


def main():
    # 读取数据
    n = int(input())
    testcases = []
    for _ in range(n):
        testcases.append(tuple(map(int, input().split())))
    # 题解
    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    # 打印答案
    for a1, a2, b1, b2 in testcases:
        path = astar((a1, a2), (b1, b2), moves)
        if path:
            print(len(path) - 1)  # path包含start，所以步数-1
        else:
            print(-1)







if __name__ == '__main__':
    main()





