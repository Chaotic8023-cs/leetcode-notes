from typing import *
from collections import Counter
import heapq


"""
最小堆：找前k个高频元素其实就是在频率数组中找最大的k个数，所以我们用一个哈希表记录频率 + 一个大小为k的最小堆记录较大的k个数即可。
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        min_heap = []
        for num, count in cnt.items():
            heapq.heappush(min_heap, (count, num))  # heapq默认按元组的第一个元素排序，所以这里先放频率，再放元素
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [x[1] for x in min_heap]  # 此时最小堆存的就是最大的那k个，我们返回全部

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
            用i指针记录了下一个比pivot小的元素应该放置的位置，一开始就是最开头的位置left
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


