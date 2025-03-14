from typing import *


"""
从右往左加，每次算当前位的结果和进位即可：结果对2求余，进位对2求商
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        carry = 0
        i, j = m - 1, n - 1
        ans = []
        while i >= 0 or j >= 0:  # 只要其中有一个数还有就继续加，当另一个位空时设成0就行
            da = int(a[i]) if i >= 0 else 0
            db = int(b[j]) if j >= 0 else 0
            res = da + db + carry
            d, carry = res % 2, res // 2  # d：当前位置应当留的结果，carry：进位
            ans.append(str(d))
            i, j = i - 1, j - 1
        if carry > 0:  # 最后如果还有进位则说明还得多一位
            ans.append(str(carry))
        return ''.join(ans)[::-1]  # 因为ans是从右往左记录的，所以最后翻转



if __name__ == '__main__':
    sol = Solution()
    a = "1010"
    b = "1011"
    print(sol.addBinary(a, b))


