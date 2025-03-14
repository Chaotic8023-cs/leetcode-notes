# https://kamacoder.com/problempage.php?pid=1046

"""
01背包：有n个不同重量不同价值的物品，每个物品只有一个，有一个最大重量为m的背包，问最多能装的价值是多少？

这个中物品第一行就对应着选第一个物品，所以需要手动初始化第一行和第一列。记忆的话看下面的2d版本！
1. dp数组下标含义：dp[i][j]表示任取物品[1,i]放到容量为j的背包中最大的价值（物品从1开始，背包容量从0开始！）
2. 递推公式：dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    对于当前物品i有两种选择：
        1. 不取物品i，则最大价值为不含物品i且背包容量为j的最大价值，即dp[i - 1][j]
        2. 取物品i，则最大价值为不含物品i且背包容量为j - weight[i]的最大价值加上物品i的价值，即dp[i - 1][j - weight[i]] + value[i]
    要注意的是如果当前物品i的重量比当前背包容量j大了，则只能不取物品i，所以要加个if判断
3. 初始化：
    一开始全初始化为0就行，因为第一列和第一行前几个放不下的都要初始化为0。其余位置随便什么值都行，因为递推公式中当前位置只跟上和左上相关
    1. 第一列dp[i][0]：所有物品放到容量为0的背包中，价值都为0，创建dp的时候就已经初始化好了。
    2. 第一行dp[0][j]：物品0放到容量递增（[0,capacity]）的背包中，放不下价值为0，放得下价值就是物品0的价值value[0]
4. 遍历顺序：因为当前是由上边和左上推出来的，所以横着遍历（先物品后背包容量）和竖着遍历（先背包容量再物品）都可以
"""
def knapsack01(num_items, weight, value, capacity):
    # 初始化：直接从第二个物品开始
    dp = [[0] * (capacity + 1) for _ in range(num_items)]
    for j in range(weight[0], capacity + 1):
        dp[0][j] = value[0]
    # 遍历
    for i in range(1, num_items):  # 物品
        for j in range(1, capacity + 1):  # 背包容量
            if j < weight[i]:  # 容量j放不下当前物品i，则只能不取物品i
                dp[i][j] = dp[i - 1][j]
            else:  # 要么不取要么取物品i
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    return dp[num_items - 1][capacity]

"""
通用版本（2D记这个）：物品也和capacity一样多加入一个0的维度，即第一行是选0个物品，这样就不用初始化第一行第一列，直接全部初始化为0即可
要注意的是此时访问weight时要用i-1，因为weight还有是用0-index，即第一个物品对应的index为0，但遍历中第一个物品index为1
"""
def knapsack01_2d(num_items, weight, value, capacity):
    # 初始化：第一行为0个物品，这样直接全部初始化为0就可以
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    # 遍历
    for i in range(1, num_items + 1):  # 物品：从第一个物品开始，第一个物品在index 1（下面访问weight时要用i-1，因为weight是0-index）
        for j in range(capacity + 1):  # 背包容量：从容量0开始遍历（虽然原始01背包问题第一列都为0，但某些题因为没初始化还是得遍历一边，所以统一记背包从0遍历！）
            dp[i][j] = dp[i - 1][j]  # 不放当前物品i
            if j >= weight[i - 1]:  # 若能放下物品i，则多比较一次（现在dp[i][j]就是不取物品i，此时max(dp[i][j], xxx)就是多和xxx比较一次，即多和取物品i比较一次）
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    return dp[num_items][capacity]


"""
1D版滚动数组，更简洁，1D记这个！
2d版本当前行总是基于上一行来进行更新的，所以不会出现问题。但是1d版本会出现物品重复使用问题，即我们更新dp[j]时，dp[j - weight[i]]已经被
当前物品i更新过一次了，所以dp[j]会再用一次物品i。通俗理解就是1d版本在更新某个位置时，前面的位置已经被更新过了，而我们需要的是旧值（即2d版本
的上一行）。解决办法是我们倒序遍历，这样所依赖的前面的值就是旧值了，就不会出现物品复用问题！
因为1D有严格的更新顺序，我们只能先正序物品后倒序背包容量！
"""
def knapsack01_1d(num_items, weight, value, capacity):
    # 初始化：同2d的情况，直接全0，对应的是2d中的第一行，即选0个物品，所以接下来我们从选第一个物品开始遍历，但此时直接用下标0开始（相当于隐晦的省略了2d中的第0行，此时第0行相当于2d中的第1行）
    dp = [0] * (capacity + 1)
    # 遍历
    for i in range(num_items):  # 物品
        for j in range(capacity, weight[i] - 1, -1):  # 背包容量（倒序）
            # 1d中就是把物品维度去掉了，所以直接把2d版本中的第一个物品维度去掉即可（注意此时我们物品的index和weight的index就对上了，0就对应的就是第一个物品）
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[capacity]


def main():
    # 读取数据
    m, n = map(int, input().split())  # m个物品，n为背包空间
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))
    # 解题
    max_value = knapsack01(m, weight, value, n)
    # 打印答案
    print(max_value)






if __name__ == '__main__':
    main()
