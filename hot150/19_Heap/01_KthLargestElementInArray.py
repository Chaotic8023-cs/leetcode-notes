# 215
from typing import *
import heapq
from collections import Counter
from itertools import count
import random


class Solution:
    """
    方法1：最小堆
    Time: O(nlogk) -> n个元素，每个元素插入heap是logk（heap只包含k个元素）
    Space: O(k) -> heap只包含k个元素
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        创建一个大小为k的最小堆，这个heap目标是保留最大的那k个元素，即正向排序好的数组的后k个元素
        当我们遍历数组的同时插入元素，如果heap超了k个元素就pop掉一个
        这样以来，当遍历完时，最小堆的root一定是第k大的元素，它下面的就是比它大的k-1个元素
        因为是最小堆，假设第k大的已经在堆里，那么堆满的时候：
            1. 第k大的在中间，pop掉的是比它小的
            2. 第k大的在root，说明比它大的k-1个已经都在堆里了，之后要是新加入一定会是比它小的，所以第k大的不会被pop掉
        """
        min_heap = []
        # 遍历整个数组，插入到min-heap中，若大小超过k则去掉当前第k大的元素，即root
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # 当遍历完整个数组时，heap的root就是整个数组第k大的元素
        return min_heap[0]

    """
    方法2：Quick Select
    设len(nums) = n，则找第k大的就是找第(n-k)小的元素，下面的描述指找第k小的元素
    注意:转换成找第(n-k)小的元素后，相当于implicitly用了0-based index，例如：
    [1,2,3,4,5,6]中第2大的为5，转换后为第(6-2)=4小的，其实这个4是0-based index，
    即从头数第5个，即最后返回的是5，所以我们转换后可以直接和pivot index作比较
    
    核心思想：
        1. 选一个pivot （一般为末尾元素，median，或随机）
        2. 把array按照pivot partition成两部分，pivot左边的都是比pivot小的，右边都是比pivot大的
        3. 根据pivot的index：
            > 1. 如果pivot index == k: 即pivot就是第k小的元素，直接返回pivot
            > 2. 如果pivot index < k: 即第k小的在右边，我们在右边继续找
            > 3. 如果pivot index > k: 即第k小的在左边，我们在左边继续找
    """
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        def partition(left, right):  # partition array [left, right], in-place
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            # move the pivot to the end
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            # partition the array
            """
          用  i指针记录了下一个比pivot小的元素应该放置的位置，一开始就是最开头的位置left
            j用来遍历[left,right)，right不看因为是pivot：
                1. 如果当前的元素nums[j] > pivot，则不用动，继续遍历
                2. 如果当前的元素nums[j] < pivot，则和位置i交换，并更新i=i+1，即i之前的元素就是比pivot小的
                   遇到下一个的话就放在更新后的i处
            """
            i = left
            for j in range(left, right):
                if nums[j] < pivot:  # 这里可以改成>来直接把array partition成左边大右边小
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            # 此时i之前的都是比pivot小的，pivot在末尾，所以直接把i处元素和pivot交换，即可完成partition
            nums[i], nums[right] = nums[right], nums[i]
            return i  # 返回pivot元素的index

        def quick_select(left, right):
            # base case: 左右指针重合
            if left == right:
                return nums[left]
            # partition the list, get the pivot index
            pivot_idx = partition(left, right)
            # check pivot index against k
            if pivot_idx == k:
                return nums[pivot_idx]
            elif pivot_idx < k:
                return quick_select(pivot_idx + 1, right)
            else:  # pivot_idx > k
                return quick_select(left, pivot_idx - 1)

        n = len(nums)
        k = n - k  # 找第k大相当于找第(n-k)小的
        return quick_select(0, n - 1)

    """
    方法3：也可以用最大堆：
    最大堆目标是保留最小的(n-k+1)个元素，即正向排序好的数组的前(n-k+1)个元素
    这样，大于target的元素就会被pop掉，最后root就是第k大的元素，下面就是比它小的n-k个元素
    +1是因为最大堆除了保留比第k大的元素小的n-k个元素，还有第k大的元素它自己
    """
    def findKthLargest2(self, nums: List[int], k: int) -> int:

        max_heap = []
        n = len(nums)
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > n-k+1:
                heapq.heappop(max_heap)
        return -max_heap[0]

    """
    方法4：Counter
    从大到小遍历counter里的数（这里为了不sort直接从最大然后每次减1来遍历），因为我们要找第k大的，所以每次把k减去当前数的个数，
    直到我们找到第k大的数，即k被某个数减到0或小于0（<0意味着当前num有多个，且其中的一个是第k大的那个）
    """
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        for i in count(max(cnt), -1):  # 返回从max(cnt)开始，每次-1的一个无穷数列 [eg: count(5, -1): 5, 4, 3, 2, 1, -1, -2...]
            k -= cnt[i]
            if k <= 0:
                return i


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 2, 1, 8, 6, 3, 5, 4]
    print(sol.findKthLargest1(nums, 2))
