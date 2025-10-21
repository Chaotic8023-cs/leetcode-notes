from typing import *


"""
从右往左加，每次算当前位的结果和进位即可：结果对2求余，进位对2求商
"""    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]  # 为方便从右往左算，先反转一下
        m, n = len(a), len(b)
        ans = ""
        carry = 0
        i, j = 0, 0
        while i < m or j < n:  # 只要其中有一个数还有就继续加，当另一个位空时设成0就行
            da = int(a[i]) if i < m else 0
            db = int(b[j]) if j < n else 0
            d = da + db + carry
            v, carry = d % 2, d // 2
            ans += str(v)
            i, j = i + 1, j + 1
        if carry:  # 最后如果还有进位则说明还得多一位
            ans += str(carry)
        return ans[::-1]  # 因为ans是从右往左记录的，所以最后翻转



if __name__ == '__main__':
    sol = Solution()
    a = "1010"
    b = "1011"
    print(sol.addBinary(a, b))


