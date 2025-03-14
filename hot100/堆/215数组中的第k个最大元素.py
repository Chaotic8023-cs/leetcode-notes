from typing import *
import heapq


"""
堆2种方法 + 快选1种方法
    1. 最小堆：存较大的k个元素，如果超容，则pop掉一个，最后堆顶就是第k大的元素，因为堆顶是较大的k个元素中最小的那个，即第k大。
    2. 最大堆：存较小的(n - k + 1)个元素，+1是因为要包含第k大的元素，如下面的例子。操作一样，超容则pop，最后堆顶就是第k大的元素，
        因为堆顶是较小的那部分中最大的，即第k大。
        例：[1,2,3,4,5]，第3大的是3，所以最大堆要存5-3+1 = 3个元素，即12还要包含第3大的3
    3. QuickSelect
"""
class Solution:
    # 最小堆
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

    # 最大堆
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)  # heapq默认从小到大排序，所以我们取反来模拟最大堆
            if len(max_heap) > len(nums) - k + 1:
                heapq.heappop(max_heap)
        return -max_heap[0]

    """
    方法3：Quick Select (第41个test过不了)
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
    def findKthLargest2(self, nums: List[int], k: int) -> int:
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



