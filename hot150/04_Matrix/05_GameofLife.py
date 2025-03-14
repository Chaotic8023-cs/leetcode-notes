# 289
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        records = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                neighbours = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                              [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
                neighbours = [v for v in neighbours if 0 <= v[0] < m and 0 <= v[1] < n]
                dic = {}
                for r, c in neighbours:
                    dic[board[r][c]] = dic.get(board[r][c], 0) + 1
                if board[i][j] == 1:
                    if dic.get(1, 0) < 2:
                        records[i][j] = 0
                    elif dic.get(1, 0) == 2 or dic.get(1, 0) == 3:
                        records[i][j] = 1
                    elif dic.get(1, 0) > 3:
                        records[i][j] = 0
                else:  # board[i][j] == 0
                    if dic.get(1, 0) == 3:
                        records[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = records[i][j]

    # O(1) space
    def gameOfLife1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        """
        如果modify in-place，后面要更新的时候前面已经覆盖掉了，所以不能直接更新。
        我们可以改变判断生死的条件：
            1. 如果board[i][j]==1且下轮为0（生转死），则设其为2
            2. 如果board[i][j]==0且下轮为1（死转生），则设其为-1
        这样就算前面是覆盖掉了，我们判断neighbours的生死时，只要大于0就是生，小于等于0就是死
        即记住了下一个state应该变成的状态，也让后面能判断当前state的状态！
        等遍历一遍完后，再遍历一遍把2的地方和-1的地方分别改成0和1即可
        """
        for i in range(m):
            for j in range(n):
                # 其实neighbours可以用for loop
                lives = -board[i][j]  # 下面算周围也把自己算了，所以抵消一下
                for r in range(i-1, i+2):
                    for c in range(j-1, j+2):
                        """
                        这里条件变成board[r][c]>0了，因为在前面不变的1算生，
                        在下轮里应变为死的（但记做2）在这轮里也是生！
                        """
                        if 0 <= r < m and 0 <= c < n and board[r][c] > 0:
                            lives += 1
                # 只用看多少个生的，其他情况都不变
                if board[i][j] == 1 and (lives < 2 or lives > 3):
                    board[i][j] = 2  # next state become dead
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = -1  # next state become live
        # 再遍历一遍更新标记2和-1的
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1






if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol = Solution()
    sol.gameOfLife(board)
    print(board)
