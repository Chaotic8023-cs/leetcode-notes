from typing import *


"""
动态规划
1. dp数组下标含义：dp[i]表示[1,i]（即i个数）能生成多少二叉搜索树
2. 递推公式： dp[i] += dp[j - 1] * dp[i - j], for j in [1, i]
    即我们枚举头节点，比如头节点4：
        1. 以1为头节点，那么左子树就是0个数字构成的二叉树的个数（因为是二叉搜索树，所以左边没有比1小的了），即dp[0]；右边就是
            3个数字构成的二叉树的个数，即dp[3]）（虽然此时数字是[2,3,4]，和dp[3]的数字[1,2,3]不同，但构型相同所以总数相同）。
            以1为头节点所能生成的二叉搜索树的总数就是左边的个数乘以右边的个数（乘法原理）。注意，0个数构成的算1个，即空树，这样另一边
            能构成几个最后乘法原理乘下来就是几个
        2. 以2为头节点，左子树就是以1个数字构成的二叉树的个数，即dp[1]；右子树就是以2个数字构成的二叉树的个数，即dp[2]。所以以2为头节点
            一共能构成dp[1] * dp[2]个
        3. 以3为头节点：左 = dp[2]，右 = dp[1]，共dp[2] * dp[1]
        4. 以4为头节点：左 = dp[3]，右 = dp[0]，共dp[3] * dp[0]
    所以n = 4时所能构成的二叉搜索树就是上面四种头节点相加
3. 初始化：只用初始化dp[0] = 1即可（空树也算一个，因为要满足乘法原理），dp[1]也能从dp[0]正常推出来（dp[1] = dp[0] * dp[0] = 1）所以不用初始化了
4. 遍历顺序：每个下标只和前面的下标有关，所以正序遍历即可
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):  # 一共i个节点，[1, i]都可以作为根节点，那么左边就有j-1个节点，右边就有i-j个节点
                """
                乘法原理：左子树种类：dp[j - 1]，右子树种类：dp[i - j]（所有数为[1,i]，此时root为j，那么左子树能选的就是[1,j-1]共j-1个数，
                右子树能选的就是[j+1,i]共i-j个数，但dp[i]其实存的就是几个数能生成几种，相对大小不影响多少种，所以直接用dp获取对应多少种即可）。
                比如[1,2,3]和[4,5,6]都是三个节点，能生成的不同树的个数也一样，所以只用看左右两边各有几个数就直接用dp几即可。
                """
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]





