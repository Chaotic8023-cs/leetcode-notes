# 909
from typing import *
from collections import deque


class Solution:
    # self try
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n ** 2

        def idx2label(pos):
            """ 把board的index转成board里的label """
            r, c = pos  # row, col
            row = n-r-1  # 因为从下到上，所以得换算到从下往上的row
            if row % 2 == 0:  # 正向（左到右）
                return n*row + c+1
            else:  # 逆向（右到左）
                return n*(row+1) - c

        def label2idx(label):
            """ 把board里的label转成board的index """
            r = label // n if label % n != 0 else label // n - 1  # 从下往上的row
            row = n - r - 1  # 从上往下的row
            if r % 2 == 0:  # 正向（左到右）
                col = label % n - 1 if label % n != 0 else n-1
            else:  # 逆向（右到左）
                col = n - label % n if label % n != 0 else 0
            return row, col

        def extract_path_len(expansions):
            count = 1  # last state in expansions is the goal
            _, from_idx = expansions[-1]
            while from_idx != 0:  # while loop only count for intermediate moves, not start
                _, from_idx = expansions[from_idx]
                count += 1
            return count

        # state(board index), come-from-idx(list index in expansions)
        visited = set()
        q = deque([((n-1, 0), None)])
        expansions = []
        while q:
            state = q.popleft()
            curr, _ = state
            if curr not in visited:
                visited.add(curr)
                expansions.append(state)
                if idx2label(curr) == target:
                    return extract_path_len(expansions)
                label = idx2label(curr)
                for dest in range(label+1, min(label+6, target)+1):
                    x, y = label2idx(dest)
                    if board[x][y] != -1:
                        q.append((label2idx(board[x][y]), len(expansions)-1))
                    else:
                        q.append(((x, y), len(expansions)-1))
        return -1


if __name__ == '__main__':
    board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
    sol = Solution()
    print(sol.snakesAndLadders(board))


