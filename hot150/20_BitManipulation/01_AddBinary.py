# 67


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]  # 从后往前算
        carry = 0
        i = 0
        res = ""
        while i < len(a) or i < len(b):
            da = int(a[i]) if i < len(a) else 0
            db = int(b[i]) if i < len(b) else 0
            v = da + db + carry
            r, carry = v % 2, v // 2  # 结果是除，carry是求余，可以用 carray, r = divmod(ans, 2)
            res += str(r)
            i += 1
        # 最后如果还有carray就加到结果中
        if carry != 0:
            res += str(carry)
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    a = "11"
    b = "1"
    print(sol.addBinary(a, b))