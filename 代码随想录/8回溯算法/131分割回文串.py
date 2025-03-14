from typing import *


class Solution:
    """
    回溯：如果枚举所有的完备切口（即完整的切割组合），会很麻烦复杂，就像下面我自己写的那样。所以我们应该一步一步来，每次从上次切完的后面开始切，
    get_next在这里其实就是剩下部分怎么切，其实就是遍历刀口的末尾元素。于是，我们定义每次的切割从start_idx开始，切到结尾i位置，当前切割出来
    的子串就是[start_idx, i]左闭右闭。所以每次遍历的结尾（i）就是range(start_idx, len(s))，我们只把当前切割下来是回文的子串加入到ans中，
    然后进行递归，下一次就从当前切割下来的子串的后面开始切，即start_idx = i + 1。这样定义的好处就是，一开始start_idx为0，那么在第一个
    循环中最后一个结尾i就是就是len(s)-1，也就是切出来的是整个字符串，即包含了字符串本身就是回文的情况！
    """
    def is_palindrome(self, s, start, end):  # 双指针看是否为回文，[start, end]左闭右闭
        l, r = start, end
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def backtracking(self, state, s, start_idx, ans):
        if start_idx == len(s):  # 终止条件：当前切割的起始位置start_idx已经超过字符串了，即已经切完了
            ans.append(state[:])

        for i in range(start_idx, len(s)):
            # 每次切一刀：从start_idx开始切，遍历当前一刀的末尾，即当前切割出来的是[start_idx, i]，左闭右闭
            if self.is_palindrome(s, start_idx, i):  # 搜索树中只加入当前切割掉的是回文的子串，这样到终止时就全是回文了
                state.append(s[start_idx: i + 1])  # 因为结尾i是闭区间，所以要包含s[i]
                self.backtracking(state, s, i + 1, ans)  # 进行递归，下次从i + 1开始切
                state.pop()


    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.backtracking([], s, 0, ans)
        return ans


"""
简洁版
"""
class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        def backtracking(start_idx, state, ans, s):
            if start_idx == len(s):
                ans.append(state[:])
                return
            for end in range(start_idx, len(s)):  # 遍历切割右端点，切[start_idx:end]左闭右闭
                if s[start_idx:end + 1] == s[start_idx:end + 1][::-1]:
                    state.append(s[start_idx:end + 1])
                    backtracking(end + 1, state, ans, s)
                    state.pop()

        ans = []
        backtracking(0, [], ans, s)
        return ans




if __name__ == '__main__':
    sol = Solution()
    s = "abb"
    print(sol.partition(s))


