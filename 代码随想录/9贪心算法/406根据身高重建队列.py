from typing import *


class Solution:
    """
    贪心：跟135分发糖果的分治思想类似，当要同时满足两个条件时，我们就一次只考虑一个。
    因为k是看前面更大的，所以我们先按身高从大到小排序，当身高一样时，k大的放后面（因为k大的前面就要有>=他的）。
    此时身高满足了，再来满足k：我们进行遍历，此时看k，因为前面都是当前身高大的，所以前面有k个就插入到index k。
    此时把小的插入到前半部分会有问题吗？不会，因为k是只看前面>=他身高的，所以小的插进去也不会造成影响。我们每次遍历到第i个，
    前面的不管怎么插入变化后都是比第i个身高大的，所以直接插入到前面第k个就能满足当前的k！

    步骤总结：
        1. 按身高倒排，身高相等时按k正排
        2. 遍历，把每个(h, k)插入到index k处即可
    """
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        # 排序：按身高倒排，按k正排
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            ans.insert(k, [h, k])  # 优化：使用 ans[k:k] = [(h, k)] 来进行插入，这样省去了调用函数insert的时间
        return ans


if __name__ == '__main__':
    sol = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(sol.reconstructQueue(people))





