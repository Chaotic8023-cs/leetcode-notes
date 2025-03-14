from typing import *


class Solution:
    """
    回溯：和131分割回文串一样，每次切割一下。只是在此题中，最多只能分成4部分，也就是最多切四下，所以我们就判断目前切出来几个（state里有几个），
    如果已经三个了，则第四个直接就能提取出来不能再切了。需要注意的是前三刀切的时候末尾位置不能遍历到len(s)，因为要给第四刀至少留一个数字！
    """
    def backtracking(self, state, s, start_idx, ans):
        if start_idx == len(s):
            ans.append('.'.join(state))

        if len(state) == 3:  # 如果当前已经有3部分了，那么第4部分不能再切割了，直接提取即可
            last_sub = s[start_idx:]
            if len(last_sub) == 1 or (last_sub[0] != '0' and int(last_sub) <= 255):
                state.append(last_sub)
                self.backtracking(state, s, len(s), ans)
                state.pop()  # 注意：这里也要把加入的第四部分pop出去，这样返回到上一层的时候才能继续递归（进去时3个，返回时也得是3个）！
        elif len(state) < 3:
            for i in range(start_idx, len(s) - 1):  # 因为要给第四部分至少留一个数字，所以遍历结尾到len(s) - 1即可
                curr_sub = s[start_idx: i + 1]
                if len(curr_sub) == 1 or (curr_sub[0] != '0' and int(curr_sub) <= 255):
                    state.append(curr_sub)
                    self.backtracking(state, s, i + 1, ans)
                    state.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.backtracking([], s, 0, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "101023"
    print(sol.restoreIpAddresses(s))


