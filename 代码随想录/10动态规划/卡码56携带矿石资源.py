# https://kamacoder.com/problempage.php?pid=1066

"""
多重背包问题：每个物品有多个。这个仅了解做题思路即可，不用记！
思路：把物品展开（看成单个物品）然后按普通01背包做：内存消耗太大；也可以用三个for循环或其它解法，不用管。
"""
def multi_knapsack(n, capacity, weight, value, count):
    # 把多个物品展开，分成单个物品
    new_weight = []
    new_value = []
    for i in range(n):
        for _ in range(count[i]):
            new_weight.append(weight[i])
            new_value.append(value[i])
    # 按普通01背包做
    dp = [0] * (capacity + 1)
    n = len(new_weight)
    for i in range(n):
        for j in range(capacity, new_weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - new_weight[i]] + new_value[i])
    return dp[capacity]


def main():
    # 读取数据
    capacity, n = map(int, input().split())
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))
    count = list(map(int, input().split()))
    # 解题
    max_value = multi_knapsack(n, capacity, weight, value, count)
    # 打印答案
    print(max_value)

if __name__ == '__main__':
    main()







