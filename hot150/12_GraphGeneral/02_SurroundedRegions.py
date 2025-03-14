# 130
from typing import *


class Solution:
    # self try
    def solve(self, board: List[List[str]]) -> None:
        """
        我们逆向思考，要找有链接的且没有连boundary的，
        那我们先在boundary上找所有O并找到和它们链接的O，
        之后board中剩下的O就是可以被surrounded的O
        """
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(board), len(board[0])
        visited = set()
        # 所有boundary上的坐标
        boundaries = ([(0, i) for i in range(n)] +
                      [(i, n - 1) for i in range(1, m)] +
                      [(m - 1, j) for j in range(n - 1)] +
                      [(i, 0) for i in range(1, m - 1)])

        def dfs(i, j, visited):
            # 和#200题类似，我们可以用直接改board，用'.'等中间值先记录一下和boundary上O链接的cell，这样就不用使用visited了
            if (i, j) not in visited:  # 因为没直接改board的值，我们需要检查visited来确保不无穷循环 (board = [O. O], [O, O])
                visited.add((i, j))  # add "O"s that connected to a boundary "O"
                for dx, dy in dxy:
                    if 0 <= i + dx < m and 0 <= j + dy < n and board[i + dx][j + dy] == "O":
                        dfs(i + dx, j + dy, visited)

        # 我们找bounday上的O，并把和它链接的O都找出来
        for i, j in boundaries:
            if board[i][j] == "O":
                dfs(i, j, visited)

        # 除去和boundary上的O有链接的，board内部的的O就都是surrounded
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"


if __name__ == '__main__':
    board = [["O","O"],["O","O"]]
    sol = Solution()
    sol.solve(board)
    print(board)
