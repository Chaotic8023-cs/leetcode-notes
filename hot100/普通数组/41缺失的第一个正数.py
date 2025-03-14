from typing import *


class Solution:
    """
    基本思路；我们把数组当成一个哈希表来记录[1,n]范围内的正整数有没有出现，其中n为数组的长度。每遇到一个数，如果它在[1,n]范围内，
    就把他它放到对应的下标处。然后再遍历一次数组，遇到第一个下标不是对应的数时，即为第一个没有出现的最小的正整数！如果都有对应的，则
    最小正整数为n + 1，因为[1, n]都有了！

    注意：为了保证不覆盖，我们把数字移动到对应位置时，用的是交换。下面是两个要注意的点：

    1. python中交换的覆盖问题：
    python中交换的写法“nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]”会先计算右边的两个值，此时因为nums[i]还是原来的值，
    所以右边两个值计算都正确。但往左边赋值时有顺序，会先赋值给第一个nums[i]，然后才是nums[nums[i] - 1]，所以nums[i]会被覆盖，导致第二次赋值中
    nums[i] - 1这个下标计算错误，已经不是原来的nums[i]了，所以我们可以交换顺序写，或用temp也行，当然第一种是最简便的！
        1> nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        2> temp = nums[i]
           nums[i], nums[temp - 1] = nums[nums[i] - 1], nums[i]

    2. 为什么用while循环？为什么是“nums[nums[i] - 1] != nums[i]”?
    用while循环是因为交换一次后当前位置交换过来的数可能还不在正确位置上，所以要继续交换，如果不交换直接看下一个下标就会漏掉某些数！
    同时我们用的条件是nums[nums[i] - 1] != nums[i]，即当前的元素nums[i]是不是没有被放到它正确的位置（下标nums[i] - 1），这
    保证了如果交换过来的新元素还没有在它正确的位置，我们就继续交换。
    那为什么不能直接检查当前的下标是否跟当前的元素对应，即"nums[i] != i + 1"?因为i + 1不一定就在数组中，所以当前位置可能永远都不会交换过来
    对应的数字，且如果有重复元素，这个条件会造成无限循环(比如[1,1]，遍历到下标1时，就会和前面一个1一直交换下去！)。
    所以我们用的是nums[nums[i] - 1] != nums[i]，即如果当前元素正确的位置已经是当前元素了，则停止交换，解决了重复元素问题，同时保证了如果新交换
    过来的元素还需要交换就能一直交换！

    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    """
    暴力解法：先筛选出所有正数，然后从小到大一个一个看有没有出现
    """
    def firstMissingPositive1(self, nums: List[int]) -> int:
        nums = set([num for num in nums if num > 0])
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1



if __name__ == '__main__':
    sol = Solution()
    nums = [1,1]
    print(sol.firstMissingPositive1(nums))
