from utils.pprintdp import pprintdp


"""
基础01背包：
有一个固定容量的背包（能装固定重量的物品），有一些不同重量的物品，每个物品价值也不同
问这个背包在不超重的情况下最大价值（每个物品只有一个，即只能装一次）
"""


def knapsack01(weights, values, knapsack_max_weight):
    # m对应i，即物品的数量，knapsack_weight对应j，即背包容量
    m = len(weights)
    dp = [[0]*(knapsack_max_weight+1) for _ in range(m)]
    """
    含义：
    dp[i][j]表示把物品[0, i]放入容量为j的背包所能获得的最大的价值
    所以如果有3个物品，背包容量为4，则dp为3*5数组（第一列为背包容量=0）
    状态转移方程：
    对于dp[i][j]，我们有两种可能：
        1. 不拿当前物品i：
            dp[i][j] = dp[i-1][j]
            即拿物品[0, i-1]，放入最大重量为j的背包所能获得的最大价值
        2. 拿当前物品i：
            dp[i][j] = dp[i-1][j-weights[i]] + values[i]
            即拿物品[0, i-1]，放入最大重量为j-weights[i]所能获得的最大价值
            加上当前物品i的价值。相当于我们先不看当前物品i，并把背包容量留出能装
            当前物品i的空余，来看不拿i且能额外装一个i时的最大价值。再加上当前物品i
            的价值即为拿了i且最大重量为j的最大价值。
    遍历顺序：
    对于此题（基础01背包），先遍历物品后遍历背包容量，和先遍历背包容量后遍历物品都可以
    因为dp[i][j]需要由上和左上来求出，先物后包（一行一行横着来）或先包后物（一列一列竖着来）
    都满足条件，上方和左上都已经有值了。
    """
    # 初始化
    """
    由于dp[i][j]是由dp[i-1][j]（前一行同一列）和 dp[i-1][j-weights[i]] + values[i]
    （前一行的左边某个）推出来的，所以我们需要初始化第一行和第一列！
    """
    """
    第一列：背包容量都是0，则价值都是0，不用初始化因为创建dp的时候就是0了
    """
    for i in range(knapsack_max_weight+1):
        """
        第一行：物品只有第一个，包容量递增，所以能放下的就是第一个物品的价值，
        放不下的就是0
        """
        if i >= weights[0]:
            dp[0][i] = values[0]
        else:
            dp[0][i] = 0
    # 遍历
    for i in range(1, m):
        for j in range(1, knapsack_max_weight+1):
            # 当前容量比物品i小，说明没法选这个物品，就会只有一种可能，即不选物品i
            if j < weights[i]:
                dp[i][j] = dp[i-1][j]
            # 当前容量>=物品i重量，说明可以装这个物品，则有两种情况，装和不装，我们选最大profit的
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
    pprintdp(dp)
    return dp[m-1][knapsack_max_weight]


"""
解法2：1维dp，把二维压缩了，也叫滚动数组
因为2维中每个dp[i][j]都是由上一行得来的，所以只用一行即可

含义：
dp[j]表示容量为j的背包最大的价值
初始化：
第一种方法就是把dp初始化成二维中的第一行，然后跳过第一个物品的循环从第二个物品开始遍历
第二种就是全部初始化为0（相当于0个物品最大的价值，即什么都不装），从第一个物品的循环开是遍历
为了方便，我们这里就用第一种

状态转移公式：
dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
相当于每次就看一行（这行就当作上一行），然后直接更新，更新完就相当于下一行了

遍历顺序：
对于二维dp，我们按先物品后背包（一行一行横着来）顺序遍历时，同一行正反遍历都可以，因为这一行仅根据上一行得来，
而上一行是已经确定的。但是现在是一维dp，如果正着遍历的话，对于一个物品i（一行），我们遍历到后面的时候
前面的j相当于已经放过物品i了，往后走的话j变大，再放i就会重复放，就错了。所以我们应该倒序遍历每个背包来确保无重复放入！

如果我们遍历顺序是先背包后物品（一列一列竖着来），二维dp是可以的，但是一维不可以。原因还是一样，
二维里我们上一行是已经确定的不会覆盖掉，但是一维的话如果两个for循环调换，即先包后物，相当于更新某个包容量之前，
前面的每个容量都（根据物品的个数）更新了多次，每个j（容量）中结果会被最后填入的一个i（物品）覆盖，结果错误！
里面本来就是倒序，然后for也换了，变成先背包后物品的话，相当于最后一个j只放入了一个物品。
"""
def knapsack01_1d(weights, values, knapsack_max_weight):
    m = len(weights)  # 物品数量
    dp = [0] * (knapsack_max_weight+1)
    """
    因为我们没初始化成二维中的第一行（即算上物品1），所以需要从第1个物品开始遍历！
    """
    for i in range(m):
        """ 这两个for不能调换，一维只能先物品后背包！"""
        for j in range(knapsack_max_weight, -1, -1):
            """ 内层遍历背包时，倒序遍历以防前面的被覆盖（即物品重复使用） """
            if j < weights[i]:  # 物品i放不下，只有一种可能（不放物品i）
                continue  # dp[j] = dp[j], 不变，所以直接跳过
            else:  # 物品i可以放下，两种情况
                dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
        print(dp)
    return dp[knapsack_max_weight]


"""
基础背包总结：
    1. 2DDP：for循环可以换，里面正倒序都可以，因为都是根据上一层来的，不存在覆盖
    2. 1DDP：for循环不能换，里面只能倒序
        for循环不能换因为：
            换了之后每个j（容量）就会被所有i（物品）更新多次，造成覆盖
        里面只能倒序因为：
            正序的话，对于每个物品i（每行），后面的j根据前面j来更新，但前面j
            已经放过一次i了，后面j变大了容量允许了，就还能放i，导致重复！
"""


if __name__ == '__main__':
    values = [15, 20, 30]
    weights = [1, 3, 4]
    max_weight = 4
    # values = [2, 3, 1, 4]
    # weights = [3, 4, 5, 6]
    # max_weight = 8
    print(knapsack01(weights, values, max_weight))
    print(knapsack01_1d(weights, values, max_weight))
