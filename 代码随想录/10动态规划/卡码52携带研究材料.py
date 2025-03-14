# https://kamacoder.com/problempage.php?pid=1052


"""
完全背包：01背包但物品有无穷多个且可以重复选多次

完全背包2d版本
"""
def knapsack_full_2d(n, weight, value, capacity):
    # 初始化
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weight[i - 1]:
                """
                01背包：
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
                完全背包：
                    dp[i][j] = max(dp[i][j], dp[i][j - weight[i - 1]] + value[i - 1])
                我们能发现多重背包里因为能复选，所以是dp[i][j - weight[i - 1]]，即包含物品i但重量少一个物品i，意思是我们已经取了几个
                物品i我们现在还想在取一个！
                """
                dp[i][j] = max(dp[i][j], dp[i][j - weight[i - 1]] + value[i - 1])
    return dp[n][capacity]

"""
完全背包1d版本：为了使物品能复用，就把01背包的1d版本中遍历背包容量改为正序即可。
"""
def knapsack_full(n, weight, value, capacity):
    # 初始化
    dp = [0] * (capacity + 1)
    # 遍历：完全背包中两个循环可以调换，但我们就统一记先物品后背包即可
    for i in range(n):  # 物品
        for j in range(weight[i], capacity + 1):  # 背包容量：正序
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[capacity]


def main():
    # 读取数据
    n, capacity = map(int, input().split())
    weight, value = [], []
    for _ in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    # 解题
    max_value = knapsack_full(n, weight, value, capacity)
    # 打印结果
    print(max_value)


if __name__ == '__main__':
    main()




