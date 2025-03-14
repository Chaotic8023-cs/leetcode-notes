# 191


class Solution:
    """
    位运算
    每次使用n & (n - 1)来清除掉n最右边的一个1：
        n-1的二进制会使得最右边的一个1变为0，然后它右边的所有0变为1，例如111000是56，减去1就变成了110111，也即是55。
        于是n & (n - 1)就可以去除n的最右边的1：111000 & 110111 = 110000
        我们每次去除最右边的1，直到n变成0为止
    """
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1
        return ans

    # Naive: 直接整二进制然后看有几个1
    def hammingWeight1(self, n: int) -> int:
        ans = ''
        while n > 0:
            ans += str(n % 2)
            n //= 2
        return ans.count("1")


