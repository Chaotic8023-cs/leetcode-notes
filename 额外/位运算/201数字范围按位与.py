from typing import *


"""
位运算：重点记 x &= x-1 是去除x最右边的一个1的方法

从left到right的所有数的后半部分是不一样的，因为是AND，所以只要有一个不一样的结果就是0
根据这个发现，我们就可以把问题转换为求公共前缀，因为后缀中肯定有两个不一样，所以后缀在AND
后就会是0

如何求公共前缀呢？我们每次去除right最右边的一个1，使得right往小变一步，直到right <= left为止。
注意right最终不一定等于left，看如下的列子：
[5,6,7]
5: 101
6: 110
7: 111
iter1： 111 -> 110，110比5大，继续
iter2: 110 -> 100，100比5小，停止

所以当right>left时我们每次去除最右边的1，最后的right就是common prefix
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 因为连续数只有最后面几位不同，所以求AND就会剩下公共前缀，所以说本题其实是求二进制下[left, right]所有数的公共前缀
        while right > left:
            right &= right - 1
        return right



