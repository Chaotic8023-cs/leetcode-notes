#  14
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            """
            以arr里第一个词s0作为基准，把每个index和剩余的词进行比较，
            在loop剩余的词时，若当前词s的长度比当前已经比较到的s0的长度小，
            或者当前s的第i个字母与s0的第i个字母不同，说明s0[:i]即为最长
            common prefix
            
            此题还能用Trie做!
            """
            for s in strs[1:]:
                if len(s) < i+1 or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]



if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

