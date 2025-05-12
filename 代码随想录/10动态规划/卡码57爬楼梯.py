# https://kamacoder.com/problempage.php?pid=1067

"""
按常规爬楼梯解，只是内层循环换成m个了，记这个常规解法即可！
"""
def climb(n, m):
    dp = [0] * (n + 1)  # 1-index
    dp[0] = 1  # 我们一开始站在第0阶，比如m=2我们一次爬两阶到2层，那么递推公式中就是dp[2] += dp[2 - 2]，所以dp[0] = 1也得算一种方法
    dp[1] = 1  # 爬1阶就一种方法（可忽略，i就从1开始循环）
    for i in range(2, n + 1):
        for j in range(1, m + 1):  # 遍历每次能爬的阶数
            if i - j >= 0:  # 确保i-j为合理下标，即能从 i-j 起步一次爬 j 阶楼梯到 i
                dp[i] += dp[i - j]
    return dp[n]

"""
按完全背包求排列解，可以不记。
"""
def climb_knapsack(n, m):
    capacity = n
    dp = [0] * (capacity + 1)
    dp[0] = 1
    # 遍历：如果出bug，就用1-index，物品背包都从1开始！这里就得从1开始！
    for j in range(1, capacity + 1):
        for i in range(1, m + 1):
            if j < i:
                continue
            dp[j] = dp[j] + dp[j - i]
    return dp[capacity]


def main():
    # 读取数据
    n, m = map(int, input().split())
    # 题解
    num_ways = climb(n, m)
    # 打印答案
    print(num_ways)

if __name__ == '__main__':
    main()


