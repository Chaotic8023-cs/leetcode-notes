# 6
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ["" for _ in range(numRows)]
        """
        模拟，curr_d_idx记录当前方向，每当走到头了就调换方向，和那个螺旋矩阵挺像
        """
        directions = [1, -1]
        # 其实可以直接用一个变量d=1记录方向，然后变的时候直接-d即可，因为只有两个方向
        curr_d_idx = 0
        i = 0  # numRows = 3 -> i: 0, 1, 2, 1, 0, 1, 2 ...
        for c in s:
            ans[i] += c
            if i+directions[curr_d_idx] >= numRows or i+directions[curr_d_idx] < 0:
                curr_d_idx = (curr_d_idx+1) % 2
            i += directions[curr_d_idx]
        return ''.join(ans)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    print(sol.convert(s, numRows))

