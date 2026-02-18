from typing import *
from collections import defaultdict


class Solution:
    """
    DFS（特殊的回溯）：此题是经典的寻找欧拉路径。直接硬记写法，就是dfs同时删除走过的边，在循环后加入ans。
    可以这么想，如果存在欧拉路径，则终点一定是第一个达成没有可去的地方（即while会结束），所以终点一定是第一个被加入到ans当中的，
    然后终点的前一站就会没地方去，加到ans中，以此类推。所以，ans最后是找到的欧拉路径的倒序。注意，字典排序和找欧拉路径无关，因为我们
    是想找字典顺序最小的那个欧拉路径，所以先sort了一下，且删除不加回。如果想找全部欧拉路径，则用经典递归（有加回的），找到一个更新一次ans。
    """
    def dfs(self, start, tickets, ans):
        while tickets[start]:  # 从当前start出发有地方可以到达
            dest = tickets[start][0]
            tickets[start].pop(0)  # 删除不加回
            self.dfs(dest, tickets, ans)
        ans.append(start)  # 在循环后加入start

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t = defaultdict(list)
        for start, end in tickets:
            t[start].append(end)
        for k in t:
            t[k].sort()  # 保证字典顺序的目的地优先
        ans = []
        self.dfs("JFK", t, ans)
        return ans[::-1]  # ans为欧拉路径的倒序


# 简化版，记这个就行
class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(g, curr, ans):
            while len(g[curr]) > 0:
                dest = g[curr].pop(0)
                dfs(g, dest, ans)
            ans.append(curr)
        
        g = defaultdict(list)
        for x, y in tickets:
            g[x].append(y)
        for k, v in g.items():
            v.sort()
        ans = []
        dfs(g, "JFK", ans)
        return ans[::-1]



if __name__ == '__main__':
    sol = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(sol.findItinerary(tickets))




