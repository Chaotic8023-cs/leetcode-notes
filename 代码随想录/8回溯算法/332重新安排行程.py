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
        while start in tickets and len(tickets[start]) > 0:  # 从当前start出发有地方可以到达
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



class Solution1:
    """
    自己写的回溯法，超时！这题其实是找欧拉路径，这里回溯法会找到所有的欧拉路径（在终止条件不直接返回的话）。其实找单一欧拉路径
    就用DFS。
    """
    def backtracking(self, state, tickets, used):
        if all(end == True for v in used.values() for end in v):
            return ["JFK"] + state[:]
        start = "JFK" if len(state) == 0 else state[-1]
        for i, end in enumerate(tickets[start]):
            if used[start][i]:
                continue
            state.append(end)
            used[start][i] = True
            ans = self.backtracking(state, tickets, used)
            if ans:
                return ans
            state.pop()
            used[start][i] = False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t = defaultdict(list)
        used = defaultdict(list)  # 就算用used也会超时！
        for start, end in tickets:
            t[start].append(end)
            used[start].append(False)
        for k in t:
            t[k].sort()  # 保证字典顺序的目的地优先
        return self.backtracking([], t, used)



if __name__ == '__main__':
    sol = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(sol.findItinerary(tickets))




