from typing import *


class Solution:
    """
    naive双指针：
    维护一个窗口[i, j]，和cnt，当 (窗口长度 - 重复次数最多的字母个数) <= k 时，即当前窗口内最少的替换方法满足k次限制，则更新一次ans。
    如果不满足，则j先不动，i右移一格继续循环。

    可以这么理解：
    对于当前窗口 [l, r]：
        窗口长度是 r - l + 1
        假设窗口里出现次数最多的字符有 max_count 个
        那么要把整个窗口变成同一个字符，最少需要修改：窗口长度 - max_count，只要它 <= k，这个窗口就是合法的。
    """
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        cnt = Counter()
        i, j = 0, 0
        ans = 0
        while i < n:
            while j < n:
                cnt[s[j]] += 1
                max_cnt = max(cnt.values())
                if (j - i + 1) - max_cnt <= k:
                    ans = max(ans, j - i + 1)
                    j += 1
                else:
                    cnt[s[j]] -= 1  # 由于i右移后第一次j先不动，这里需要抵消下次进入循环对j的cnt的更新
                    break
            cnt[s[i]] -= 1
            i += 1
        return ans
    
    """
    优化版（记这个）：
    naive版中每次求max_cnt太慢。我们显式维护max_cnt，并将滑窗改为更通用、合适的方式：
    每次右端点j+=1，接着更新max_cnt。然后只要不符合条件，一直右移左端点i直到当前窗口满足条件，更新ans。

    经典滑窗模版：
    for r in range(n):
        1. 先把 s[r] 纳入窗口

        2. 如果窗口不合法：
            不断移动左端点 l
            直到窗口重新合法

        3. 此时窗口合法，更新答案
    """
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        cnt = Counter()
        max_cnt = 0
        i = 0
        for j in range(n):
            cnt[s[j]] += 1
            max_cnt = max(max_cnt, cnt[s[j]])
            while (j - i + 1) - max_cnt > k:
                cnt[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans



