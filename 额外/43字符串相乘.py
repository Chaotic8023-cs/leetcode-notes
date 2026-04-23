from typing import *


"""
和字符串相加不一样，虽然还是采用大竖式，但乘法不是一次能算完的

index:  4   3   2    1    0

                1    2    3
                4    5    6
        --------------------
                6    12   18
            5   10   15
        4   8   12
        --------------------
add     4   13  28   27   18
        --------------------
carry:  5   6   0    8    8      

具体的算法是拿第二个数的每一位和第一个数的每一位相乘，结果写到对应位置上，关系位num1[i] * num2[j]写到res[i+j]上。
然后再统一处理进位，得到结果，最终反转再去除前导0。
时间复杂度O(m * n)，空间O(m + n)

注：因为谁作为大竖式中第2个数都行，所以真正写的时候不需要考虑大竖式中num1和num2的位置关系，直接两个for遍历就行！
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]  # 先反转，方便处理下标
        m, n = len(num1), len(num2)
        res = [0] * (m + n)  # 结果最多m+n位
        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1[i]) * int(num2[j])  # 第i位和第j位的乘积加到结果中的第(i+j)位上
        # 最后统一处理carry
        carry = 0
        for i in range(m + n):
            d = res[i] + carry
            v, carry = d % 10, d // 10
            res[i] = v
        # 拼成结果然后反转，再去掉前导0
        ans = ''.join(str(x) for x in res)[::-1].lstrip('0')
        # 返回结果时处理下结果为0被全strip掉的情况
        return ans if ans else '0'
        