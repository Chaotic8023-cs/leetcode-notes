from typing import *


class Solution:
    """
    1循环+双指针：用i遍历数组，表示第一个数，同时用两个指针left和right在当前数组的后半部分[i+1:]表示第二个和第三个数。我们在遍历i的时候就对i去重，
    同时找到一个答案后对left和right去重。去重就是看之后的位置的数和当前的答案有没有重复，如果重复就跳过。

    此题中只让返回数组中的元素而并非下标，所以一开始先将数组进行排序，使得数组后半部分使可以使用双指针！
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)  # 对数组进行排序
        ans = []
        for i in range(n):  # 用i遍历，表示第一个数
            if nums[i] > 0:  # 剪枝：在非递减数列里如果第一个数都比0大，那么后面的就不用找了，因为和不可能小于0了（可省略）
                break
            # i去重：如过当前的i和之前用过的i（i-1）重复则跳过，保证了unique的i
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1  # 在数组后半部分使用双指针，left和right表示第2和第3个数
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:  # s == 0，满足题目条件
                    # 更新ans
                    ans.append([nums[i], nums[left], nums[right]])
                    # left和right都更新一位
                    left, right = left + 1, right - 1
                    """
                    left和right去重: 即left的右边和right的左边只要和刚才加入到ans中的left和right相等，则跳过
                    
                    这里原来用的第一个条件是while left < n和while right >= 0，但其实我们没必要一直跳过并找到第一个
                    和当前答案中的left和right不重复的地方，其实当left和right不满足left < right时，就可以提前停止
                    """
                    while left < right and nums[left] == nums[left - 1]:  # left和刚才的（left-1）比
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:  # right和刚才的（right+1）比
                        right -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))
