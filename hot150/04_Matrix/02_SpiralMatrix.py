# 54
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    # 暴力模拟，自己写了好久，很不推荐！
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        boundM, boundN = m, n
        startM, startN = 0, 0
        """
        以能走一圈为前提，即 右->下->左->上 走四次
        一直走到不能走完整的一圈为止
        """
        while boundN > startN+1 and boundM > startM+2:
            i = startM
            for j in range(startN, boundN, 1):
                res.append(matrix[i][j])

            j = boundN-1
            for i in range(startM+1, boundM, 1):
                res.append(matrix[i][j])

            i = boundM-1
            for j in range(boundN-2, startN-1, -1):
                res.append(matrix[i][j])

            j = startN
            for i in range(boundM-2, startM, -1):
                res.append(matrix[i][j])

            boundM, boundN = boundM-1, boundN-1
            startM, startN = startM+1, startN+1

        """
        然后剩余的根据四步中的每一步的条件来判断能否继续走下去：
        即能走第一步则走第一步，在能走第一步的前提下看能不能走
        第二步，一次类推
        走下一步必须建立在能走上一步的前提下！因为通过这个方法
        是通过记录start和end来限制ij，但是后面可能会和前面走的
        重复，如果不限制前面已经走了的话。
        """
        if startN < boundN:
            i = startM
            for j in range(startN, boundN, 1):
                res.append(matrix[i][j])

            if startM+1 < boundM:
                j = boundN - 1
                for i in range(startM + 1, boundM, 1):
                    res.append(matrix[i][j])

                if boundN-2 > startN-1:
                    i = boundM - 1
                    for j in range(boundN - 2, startN - 1, -1):
                        res.append(matrix[i][j])

                    if boundM - 2 > startM:
                        j = startN
                        for i in range(boundM - 2, startM, -1):
                            res.append(matrix[i][j])

        return res

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0  # current pos
        """
        directions: 当前的移动方向，一共四个方向，每个方向两个数是
        i和j的移动方向，比如一开始的横着走，即i不变j每次加一（[0, 1]）
        我们一直按当前方向走，然后每次走完一步将当前的格子加入visited，
        然后我们算出下一步的坐标，判断是否在矩阵内，且没有visited，如果满足
        则继续朝当前方向走。
        如果不满足，则要们因为沿着当前方向走出去了（超出matrix的size了），要么
        因为当前方向的下一格子已经走过了（即碰到了外圈），我们就改变方向继续走。
        一共走m*n步即可！
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0  # 当前方向
        visited = set()
        ans = []
        for _ in range(m * n):
            ans.append(matrix[i][j])
            visited.add((i, j))
            next_i, next_j = i + directions[d][0], j + directions[d][1]
            if not 0 <= next_i < m or not 0 <= next_j < n or (next_i, next_j) in visited:
                d = (d+1) % 4
            i += directions[d][0]
            j += directions[d][1]
        return ans


if __name__ == '__main__':
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    # matrix = [[1, 2, 3, 4]]

    # matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

    matrix = [[1]]

    sol = Solution()
    print(sol.spiralOrder1(matrix))

