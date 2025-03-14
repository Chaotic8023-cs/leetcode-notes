from typing import *
# https://programmercarl.com/kamacoder/0098.%E6%89%80%E6%9C%89%E5%8F%AF%E8%BE%BE%E8%B7%AF%E5%BE%84.html


class Solution:
    """
    DFS：用类似回溯的递归实现DFS即可
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(n, path, ans):
            if n == len(graph)-1:
                ans.append(path[:])
            for i in graph[n]:
                dfs(i, path + [i], ans)  # 没用append，所以不需要回溯

        ans = []
        dfs(0, [0], ans)
        return ans

    """
    有回溯的DFS写法
    """
    def allPathsSourceTarget1(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(n, path, ans):
            if n == len(graph) - 1:
                ans.append(path[:])
            for i in graph[n]:
                path.append(i)
                dfs(i, path, ans)
                path.pop()

        ans = []
        dfs(0, [0], ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    graph = [[1, 2], [3], [3], []]
    print(sol.allPathsSourceTarget(graph))





