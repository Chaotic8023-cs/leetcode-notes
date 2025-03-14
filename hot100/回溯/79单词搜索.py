from typing import *


"""
下面Solution2中的暴力解法的优化版本：
    1. 每次只比较字母，效率高
    2. 有剪枝，如果当前字母已经不是word里的就提前返回
    3. 直接在board中标记已经访问过的，不用额外的visited数组，更高效
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, k):
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if board[i][j] != word[k]:  # 剪枝：如果当前字母不等于第k个字母（0-index），则提前返回
                return False
            c = board[i][j]
            board[i][j] = '0'  # 标记当前位置已访问
            for dx, dy in dirs:
                next_x, next_y = i + dx, j + dy
                if 0 <= next_x < m and 0 <= next_y < n and board[next_x][next_y] != '0':
                    found = dfs(next_x, next_y, k + 1)
                    if found:
                        return True
            board[i][j] = c  # 回溯：取消标记以访问
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


"""
Solution中第三个改回visited数组，也能过
因为visited是提前标记下一个地方，所以for循环中每次回来就得取消标记；优化版本直接在board标记是记录当前位置已经来过，所以在for循环中不需要回溯，
因为for循环中是往下一个位置走，在for循环结束的时候才需要回溯。
"""
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, k, visited):
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if board[i][j] != word[k]:  # 剪枝：如果当前字母不等于第k个字母（0-index），则提前返回
                return False
            for dx, dy in dirs:
                next_x, next_y = i + dx, j + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    found = dfs(next_x, next_y, k + 1, visited)
                    if found:
                        return True
                    visited[next_x][next_y] = False
            return False

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                visited[i][j] = True
                if dfs(i, j, 0, visited):
                    return True
        return False


"""
Solution1中visited数组其实也可以像优化版本中每次标记当前位置，这样for循环结束才需要回溯。
"""
class Solution1_:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, k, visited):
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if board[i][j] != word[k]:  # 剪枝：如果当前字母不等于第k个字母（0-index），则提前返回
                return False
            visited[i][j] = True  # 标记当前位置
            for dx, dy in dirs:
                next_x, next_y = i + dx, j + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
                    found = dfs(next_x, next_y, k + 1, visited)
                    if found:
                        return True
            visited[i][j] = False  # 回溯
            return False

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                if dfs(i, j, 0, visited):
                    return True
        return False


"""
暴力解法：在每个位置跑一次dfs。
会超时，因为：
    1. 字符串匹配效率低：在dfs中，你频繁地调用''.join(state)将state转换为字符串，然后与word比较。这在递归过程中会带来额外的开销。
    2. 未提前剪枝：即使已经发现当前路径不可能匹配word，代码仍然继续尝试其他路径。
    3. visited矩阵创建效率低：每次递归调用中都会重新创建visited矩阵，这会增加运行时间。
"""
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, state, visited):
            if ''.join(state) == word:
                return True
            if len(state) == len(word):
                return False
            for dx, dy in dirs:
                next_x, next_y = i + dx, j + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
                    state.append(board[next_x][next_y])
                    visited[next_x][next_y] = True
                    found = dfs(next_x, next_y, state, visited)
                    if found:
                        return True
                    visited[next_x][next_y] = False
                    state.pop()

        for i in range(m):
            for j in range(n):
                # 到一个位置后确保state已经有那个位置的字母，且visited已经标记，这样方便检查，所以初始时state就包含出发点的字母且已经visited了！
                state = [board[i][j]]
                visited = [[False] * n for _ in range(m)]
                visited[i][j] = True
                found = dfs(i, j, state, visited)
                if found:
                    return True
        return False





