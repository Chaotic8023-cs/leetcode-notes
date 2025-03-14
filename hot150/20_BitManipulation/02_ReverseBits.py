# 190


"""
给一个32位的int n，把它的二进制bits反转，并输出二进制反转后的int
"""
class Solution:
    """
    位运算：从右往左把bit移动到结果的对应位置上
    1. 得到Least Significant Bit (LSB): (n & 1)
        用n和1作bit-wise and，例如n为5，二进制就是101，和1作and就是：101和001作and，结果就是001，
        也就是只保留最右边的bit（前面都是0，所以结果一定是0，最右边的bit和1作and，所以原来是几结果就是几）
    2. 把最右边的bit shift到反转后的对应位置：(n & 1) << (31 - i)，即把(n & 1) left shift (31 - i)位
        例如100，我们先得到最右边的bit为0，那么反转后是001，即最右边的bit需要往左shift两位，所以从右往左数的第
        i个bit要往左shift (31-i)位
    3. 更新ans：ans |= (n & 1) << (31 - i)， 即ans = ans | (n & 1) << (31 - i)
        一开始ans为0，为了只更新一个bit，我们用bit-wise or。例如n为101，先取LSB=1，shift到对应位置后得到的
        是100，所以作bit-wise or就是 000 | 100 = 100，即把1放在了ans中最左边。也就是说我们在二进制下更新
        那个反转过来的1个bit
    4. 通过right shift去掉当前的LSB，使得下一个循环中能取到LSB左边的一个bit: n >>= 1



    注意：ans |= (n & 1) << i最好是用ans += (n & 1) << i。
    |=是bitwise OR，因为本题每次每次过来的位是不同的位，所以|=不会出现两个相同位置都是1的情况。
    如果两个数相同位置都是1，那么|=就不会进位，只会进行OR操作，就会出问题，但本题因为每次只看1位，不会重叠，所以不会有问题。
    例子：
    110 |= 001 = 111 = 7，6 |= 1 = 7。此时没有两位都是1，所以和+=一样。
    101 |= 111 = 111 = 7，5 |= 7 = 7。此时有两位都是1的，所以和+=不一样。
    """
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= (n & 1) << (31 - i)
            n >>= 1
        return ans

    # naive：手动算（不用看）
    def reverseBits1(self, n: int) -> int:
        # 首先得到n的2进制，并加上padding（# 通过求余的方法得到的res已经是反过来的，所以可以直接用）
        res = ""
        while n > 0:
            res += str(n % 2)
            n //= 2
        num_padding = 32 - len(res)
        if num_padding > 0:
            res += '0' * num_padding
        # 再算反转后的数的十进制
        p = 0  # power
        ans = 0
        for i in range(len(res)-1, -1, -1):
            ans += 2 ** p if res[i] == '1' else 0
            p += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseBits(0))
    # print(sol.reverseBits(43261596))
