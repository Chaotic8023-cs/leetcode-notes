from typing import *


"""
方法一：贪心（记这个，好记!）
维护两个变量 up 和 down 来分别记录以“上升”结尾和以“下降”结尾的最长摆动子序列的长度。
初始时up, down = 1, 1，因为最长的摆动序列至少有一个元素。
    up: 表示当前序列最后一次差值为正（即上升）的最长摆动序列长度。
    down: 表示当前序列最后一次差值为负（即下降）的最长摆动序列长度。
遍历过程中，针对每一对相邻的数字，我们有三种情况：
    1. nums[i] > nums[i - 1]
        当前数字比前一个大，说明出现了一个上升的摆动。要使序列满足摆动要求，之前的摆动应该是下降（即最后一次差值为负）。
        因此，我们可以在之前下降序列的基础上加上这个上升，更新 up = down + 1。
    2. nums[i] < nums[i - 1]
        当前数字比前一个小，说明出现了一个下降的摆动。此时，为了保证交替，需要之前的摆动是上升的，所以更新 down = up + 1。
    3. nums[i] == nums[i - 1]
        相等的情况不构成摆动，所以不更新任何状态。
最后返回 up 和 down 中较大的那个，即为最长摆动子序列的长度。
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = 1, 1
        for i in range(n - 1):  # 只需要看数组中两两之间的差值，所以用 for i in range(1, n)然后比较nums[i]和nums[i - 1]也行！
            if nums[i] < nums[i + 1]:
                up = down + 1
            elif nums[i] > nums[i + 1]:
                down = up + 1
        return max(up, down)


"""
方法2：找极值点
其实相当于只记录峰值元素（找极值）.
"""
class Solution1:
    """
    我们默认结尾算1个（跟把第一个算1个同理），初始化ans=1，然后遍历前n-1个元素通过看每个元素两边的坡度看是否它是极值点。
    因为第一个元素前面没有元素，所以可以给前面补一个一样的元素，但其实不用真补，一开始设prev_diff = 0即可。这样我们其实
    就是删除前面的单调或重复的元素，只保留最后的那个极值：
        例如 1 -> 2 -> 2 -> 1，我们除了在两边出现纯的一正一负外，只记录先平后正负，即第一个1是先平后加，最后一个2是先平后减，
        也就是说前面的一个2被排除了。这样就相当于去除了平的情况。
    需要注意的是还有特殊的情况就是 1 -> 2 -> 2 -> 3 -> 5，即先增后平再增，如果我们每次更新prev_diff = next_diff，那么
    1 -> 2和2 -> 3都会被算（因为都是先平后增），所以我们仅在找到极值点的时候更新prev_diff，

    """
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        prev_diff = 0  # i和i-1的diff，即和前一个元素的diff
        ans = 1  # 默认最后一个元素在结果（和默认第一个元素在同理，但因为往前补元素不用真补，直接用prev_diff代替，更方便，所以默认选最后的一个元素）
        for i in range(n - 1):
            next_diff = nums[i + 1] - nums[i]
            if (prev_diff <= 0 and next_diff > 0) or (prev_diff >= 0 and next_diff < 0):  # 除一正一负，我们只算先平后变化的，实际上就是只算重复元素的最后一个
                ans += 1
                prev_diff = next_diff  # 仅在找到极值点时更新
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(sol.wiggleMaxLength(nums))



