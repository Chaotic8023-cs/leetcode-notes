from typing import *


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


"""
通用解法：

这套方法其实是一种**二进制抽样方法，它的主要步骤是：

1. 利用已有的 rand 函数构造一个等概率产生 0 和 1 的随机函数 rand2()。  
    1.1 若n为偶数，如4，则可以直接按照奇偶来生成：[1, 3] -> 1, [2, 4] -> 0，即直接返回n % 2。
    2.2 若n为奇数，如5，则拒绝5，接受[1,4]，然后按偶数做即可。

2. 根据目标范围上界 n 来决定需要的二进制位数 k，用 rand2() 生成 k 位二进制数，从而生成 [0, 2^k-1] 之间的均匀整数。

3. 如果生成的数在 [0, n - 1]的范围内，则接受（[0, n - 1]可以映射到[1, n]）；否则拒绝并重新生成。

这种方法是非常通用的，理论上可以将任意一个 rand 函数（只要它能构造出均匀的二进制位）转换成另一个目标范围内的均匀随机数。只要满足：
- 能够构造等概率的二进制输出，  
- 拒绝采样能使得最终输出的集合大小正好是目标集合的大小，  
就能保证每个合法结果出现的概率相同。
"""
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # 确定要生成的上界（10）至少需要几位二进制数来表示，这里我们生成[0, 9]即可，最后映射到[1, 10]就行，所以能表示9就行
        n = 1
        while 2 ** n - 1 < 9:
            n += 1
        # 拒绝采样：使用rand2()生成4位二进制数，即[0, 15]，拒绝[10, 15]，接受[0, 9]
        while True:
            num = 0
            # 使用rand2()生成n = 4位二进制数的每一位
            for _ in range(n):
                # 左移一位，并加入新生成的二进制位
                num = (num << 1) | self.rand2()
            # 若生成的数字在0~9之间，则映射到1~10
            if num < 10:
                return num + 1

    def rand2(self):
        while True:
            x = rand7()
            if x != 7:
                """
                使用拒绝采样构造rand2():对于rand7()生成的[1,6]。当x为1,3,5时，x % 2 == 1；当x为2,4,6时，x % 2 == 0。拒绝7之后，0和1各自的概率均为1/2

                对于rand7()生成的[1, 7]，我们只要[1, 6]，拒绝7.
                对[1, 6]的数分为两组：
                    1. [1, 3, 5]输出1
                    2. [2, 4, 6]输出0
                这样输出1和0就是等概率的
                    条件概率：P(A|B) = P(A & B) / P(B) = (3/7) / (6/7) = 1/2
                        - P(A)：生成的数在[1,3,5]（或[2,4,6]）的概率 = 3/7
                        - P(B)：rand7()生成的数符合我们要求，即在[1, 6]的概率 = 6/7
                        - P(A & B)：由于A被B包含了，所以生成的数在[1,3,5]（或[2,4,6]）的概率就是3/7
                """
                return x % 2


