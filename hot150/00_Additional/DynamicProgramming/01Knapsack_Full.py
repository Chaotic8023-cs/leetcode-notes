from utils.pprintdp import pprintdp


"""
完全01背包：
有一个固定容量的背包（能装固定重量的物品），有一些不同重量的物品，每个物品价值也不同
问这个背包在不超重的情况下最大价值（每个物品有无数个，即同一物品可以装多次）
"""

"""
注意，01背包的2d在完全背包不适用，因为：
    01背包中的dp[i][j]表示物品为[0, i]背包容量为j时的最大价值，
    有个问题是当我们更新dp[i][j]时，我们看的是i-1行，即没有物品i时
    或只放一次物品i时的最大价值。可是完全背包一个物品能放多次，就没有算
    上多次放当前i的情况，导致错误。
    
    例：
        weights: [1,2,3], values: [10, 30, 40], max_weight = 6
        当我们考虑j=4时，用01背包的2d逻辑更新的话（就算第一行初始化变成可以放多个物品1），
        在更新第二行时（i=1，j=4），结果是放2个物品1和一个物品2，最大价值50。可是正确的最大价值
        是放两个物品2得来的60。
    
    所以用一维dp是为了在更新后面的j时，我们参考的前面的j是允许同一物品放多次的最大价值！
    也就是说完全背包里dp[j]表示允许放多次同一物品的情况下的最大价值。
"""


"""
先物品后背包
"""
def knapsack_full_1d(weights, values, knapsack_max_weight):
    m = len(weights)  # 物品数量
    dp = [0] * (knapsack_max_weight+1)
    for i in range(m):
        for j in range(0, knapsack_max_weight+1):  # 内循环（背包容量）必须正序！
            if j < weights[i]:  # 物品i放不下，只有一种可能（不放物品i）
                continue  # dp[j] = dp[j], 不变，所以直接跳过
            else:  # 物品i可以放下，两种情况
                dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
        print(dp)
    return dp[knapsack_max_weight]


"""
先背包后物品
"""
def knapsack_full_1d_(weights, values, knapsack_max_weight):
    m = len(weights)  # 物品数量
    dp = [0] * (knapsack_max_weight+1)
    for j in range(0, knapsack_max_weight+1):  # 背包容量必须正序！
        """
        因为这里内循环是物品，正反都行，因为后面j仅依赖前面j，
        对于同一个j，选物品放的时候是等效的。我们默认用正向即可。
        """
        for i in range(m):
            if j < weights[i]:  # 物品i放不下，只有一种可能（不放物品i）
                continue  # dp[j] = dp[j], 不变，所以直接跳过
            else:  # 物品i可以放下，两种情况
                dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
        print(dp)
    return dp[knapsack_max_weight]


"""
完全背包总结：
就是一维01背包把内循环的倒序换成正序即可（但forloop可以调换）！

for循环可以换：
    因为一维里每个j都是根据前面的j来更新的，所以就算先背包后物品，在行的角度来看
    后面j更新的时候前面j已经更新完了，不会有问题！
背包容量只能正向：
    保证前面的物品可以被多次使用。这个还保证了每次更新j时，前面的j一定是允许重复放的
    最大价值。
    因为后面depend on前面，所以物品能重复使用的情况下，一定得保证背包容量j是正序遍历，这样才能
    遍历到j时，前面的已经是能多次放物品的最大价值了！
"""
if __name__ == '__main__':
    values = [10, 30, 50]
    weights = [1, 2, 3]
    max_weight = 6
    # values = [2, 3, 1, 4]
    # weights = [3, 4, 5, 6]
    # max_weight = 4
    print(knapsack_full_1d(weights, values, max_weight))
    print(knapsack_full_1d_(weights, values, max_weight))
