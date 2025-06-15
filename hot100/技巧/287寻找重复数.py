from typing import *


"""
O(n) time O(1) space，记这个！
和#41题第一个缺失的整数思路一样：
    我们规定数组下标i存放数i + 1，即0放1，1放2，...
    遍历数组每个下标i（n + 1所有位置都遍历），如果：
        当前元素(nums[i]) 应当放到的那个下标处(nums[i] - 1) 不是当前元素，则把当前元素放到它应该放到的位置上（swap）。
    最后，数组的最后一个元素就一定是重复数。
    
和#442题数组中重复的数据的区别：442中虽然数字范围还是[1, n]，但是nums长度为n，且可能有多个数重复两次，所以swap完后，要再遍历一次，
收集所有nums[i] != i + 1的数，即为重复数
    
重要：
为什么while条件不能判断当前的下标i上元素不是i + 1，即 while nums[i] != i + 1
原因和41题类似，可能出现无穷循环，例如：
    [3, 1, 3, 4, 2]
在i = 1时，判断nums[i] != i + 1，即nums[0] != 1，我们就会把当前元素放到它应该放到的下标上，然后期待换过来的就是1。
但是，当前的3应该放到下标2处，但下标2处恰好还是3，也就是重复数，这样最后就会造成两个3一直交换！
所以：
    我们改成判断当前元素应当放到的下标是不是已经是当前元素了，即nums[nums[i] - 1] != nums[i]，如果是就跳过。
    
等我们遍历完n + 1个元素后，我们能确保[1, n]这n个数一定在下标[0, n - 1]上，所以最后一个一定就是重复数。
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 使用传统swap逻辑更清楚，同时不会因为pythonic写法造成问题！
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        n = len(nums)
        for i in range(n):
            while nums[nums[i] - 1] != nums[i]:
                swap(nums[i] - 1, i)
        return nums[-1]


"""
真正符合题意的解法，不改动数组且空间O(1)，时间为O(n)。
思路是看成环形链表2：nums长度为n+1，则我们将下标看作节点，即[0, n]一共 n+1 个节点；将nums[i]看作next指针，即下标i指向的是nums[i]。
由于题中说明nums[i]的范围是[1, n]，所以不会出现越界的情况。由于某个数会重复，所以就有多个指针指向这个数，最终会形成环，而环的入口就是这个重复数。
我们就可以用环形链表2的解法来解决次题。
"""
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0  # 从第一个节点出发，即下标0
        while True:  # 由于不会走到头，所以用while True就行
            # nums[i]就相当于i.next
            slow = nums[slow]  # slow走一步
            fast = nums[nums[fast]]  # fast走两步
            # 相遇时再用同样的方法找到环入口
            if slow == fast:
                i, j = 0, slow
                while i != j:
                    i, j = nums[i], nums[j]
                return i


"""
二分：O(1)额外空间，O(nlogn)时间
原理：因为数字范围是[1, n]，那么对于某个数字x，如果整个数组中 <=x 的数字的个数大于x，则说明数字范围[1,x]中有重复数字，否则[x+1,n]中有重复数字。
例如：[2, 3, 1, 2, 4]，对于数字2，小于等于2的有1,2,2，一共三个，如果2不重复则为1,2两个。此时就说明数字范围[1,2]中出现重复数字了。
所以我们就可以二分搜索，统一左开右闭，数字的范围是[1, n]所以left = 1，right=len(nums)，也就是right = n + 1。注意我们二分是直接分数字[1,n]，
不是下标！
"""
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        while left < right:
            mid = (left + right) >> 1
            count = sum(1 for num in nums if num <= mid)  # 统计 <= mid的数字个数
            if count > mid:  # 数字范围[1, mid]中出现重复
                right = mid
            else:  # count <= mid：数字范围[mid + 1, n]中出现重复
                left = mid + 1
        return left  # 一般都是直接return left，因为最后走的是left = mid + 1，那时候mid为两个挨着的数左边那个，条件为count <= mid，即左边那个数没重复，所以最后就是右边那个数，即left+1后的left


"""
抽屉原理：如果n个东西放到m个抽屉中，n > m，则至少有一个抽屉有>=2个物品
这个是原地解法，会对数组进行改动，不符合题意，但是很巧妙
因为数组长度为n + 1，数字范围是[1, n]，所以所有非重复数字都能放到下标[1, n]上不存在越界问题。
所以我们就把每个数字放到对应的位置上（放到对应的抽屉中），最后如果某个数字要放的对应的抽屉已经放过了，则这个数字就是重复的。

具体实现方法：
下标代表抽屉：放之前（修改nums[i]之前），先把nums[i]的数存下来作为下一个要放的数，然后再标记nums[i] = 0，意味着抽屉i已经放过了。因为数的范围是[1, n]，
所以抽屉0没用，同时我们应该先从nums中第一个数开始，即下标0，所以一开始我们从0开始（虽然一开始给抽屉0存放多余，但是统一了逻辑）。
"""
class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            if nums[i] == 0:
                return i
            next_num_to_put = nums[i]  # 修改数nums[i]前记录下一个要放的数
            nums[i] = 0  # 把数字i存放到当前抽屉i
            i = next_num_to_put  # 更新i为下一个要放的数

