from typing import *


"""
实际就是给s的每一位标记就好了：假设numRows为4，那就是那s每一位的行数就是：1234321234321
我们先构造一个flag，然后再逐行加入到ans中即可
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:  # 对于numRows == 1的情况直接返回s即可，因为下面生成的flag此时会有问题
            return s
        flag = []
        direction = 1
        curr = 0
        for i in range(n):
            flag.append(curr)
            if curr == numRows - 1:
                direction = -1
            elif curr == 0:
                direction = 1
            curr += direction
        # 先加入第0行的元素，接下来第1行，以此类推
        ans = ""
        for i in range(numRows):
            for j in range(len(flag)):
                if flag[j] == i:
                    ans += s[j]
        return ans


"""
优化版：和上面的思路一样，只是我们直接为每行（numRows）初始化一个空字符串，然后遍历s，append到对应行上，最后join一下即可。
"""
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [""] * numRows
        i, dx = 0, -1  # i是当前的flag；dx是当前的direction，初始化成-1以适配if的取反，这样第一次进去方向就会变成1
        for c in s:
            ans[i] += c
            if i == 0 or i == numRows - 1:
                dx = -dx
            i += dx
        return ''.join(ans)


if __name__ == '__main__':
    sol = Solution1()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))

