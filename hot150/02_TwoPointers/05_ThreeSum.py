# 15
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        """
        我们先sort array（方便跳过重复的元素），然后对于每一个nums[i]（fst）
        问题就变成一个target = -nums[i]的2sum
        在sort的情况下我们就可以用2pointer，令j和k分别为当前i右边
        部分的开头和结尾，然后找sum等于target的两个元素。
        当当前的sum小于target的时候，则j右移，若大于则k左移动。
        如果找到了一组ij的sum等于target，则加入ans，并继续找（i+1, k-1）
        需要注意的是要排除duplicates：
            1. 外层循环：若当前fst和上一个fst一样，则跳过
            因为在前一个循环里，以fst为第一个数字的所有triplet已经找全！
            2. 内层循环：找到target需要更新ans时，若当前的j和上一个j一样，则跳过
            因为在fst和j固定的情况下，k一定一样，所以当前的j重复了的话，结果一定重复，
            所以跳过
        """
        for i in range(n-2):  # 这里其实只用loop到n-2，但是后面设定jk时候保证了它们都在n以内
            fst = nums[i]
            if fst > 0:
                break  # fst都大于0了，之后的都是大于fst的，所以自此不可能找到和为0的了
            if i > 0 and fst == nums[i-1]:  # fst重复，跳过
                continue
            target = -fst
            j, k = i+1, n-1  # 保证了index合法
            while j < k:
                s = nums[j]+nums[k]
                if s == target:
                    if j == i+1 or nums[j] != nums[j-1]:
                        # 只有当j是第一个j，或（之后的j）和前一个j不重复时，这个triplet才是unique
                        res.append([fst, nums[j], nums[k]])
                    j, k = j+1, k-1
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return res


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(nums))

