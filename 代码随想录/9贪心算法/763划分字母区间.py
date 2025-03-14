from typing import *


class Solution:
    """
    贪心：因为要分割尽可能多，所以我们每次分割出来的长度尽可能短。我们先统计所有字母最后一次出现的位置，这样，一开始我们能分割出最小的长度
    就是到第一个字母最后一次出现的位置。但是，这中间还有其他字母，其last pos可能超出第一个字母的last pos，所以，我们每次一开始设curr_max等于
    第一个字母的last pos，然后遍历到curr_max，边遍历边看中间出现的其他字母的last pos是否超出curr_max，如果超出即把当前的切割点扩展那个字母的last pos。

    思路总结：每次取第一个字母开始的最小的子串（通过记录last pos），同时满足中间出现的其他字母的last pos（对一开始第一个字母的last pos进行扩展）
    """
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        i = 0
        ans = []
        while i < n:
            start = i  # 每次选当前第一个字母
            curr_max = last[s[i]]  # curr_max设为第一个字母最后出现的位置（即尽可能的分割更小的子串）
            # 同时对于中间出现的字母，如果它们的last pos超出了curr_max，则扩展curr_max
            i += 1
            while i <= curr_max:
                curr_max = max(curr_max, last[s[i]])
                i += 1
            ans.append(i - start)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "ababcbacadefegdehijhklij"
    print(sol.partitionLabels(s))


