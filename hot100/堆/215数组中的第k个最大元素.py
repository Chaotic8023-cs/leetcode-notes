from typing import *
import heapq


"""
堆2种方法 + 快选1种方法
    1. 最小堆：存较大的k个元素，如果超容，则pop掉一个，最后堆顶就是第k大的元素，因为堆顶是较大的k个元素中最小的那个，即第k大。
    2. 最大堆：存较小的(n - k + 1)个元素，+1是因为要包含第k大的元素，如下面的例子。操作一样，超容则pop，最后堆顶就是第k大的元素，
        因为堆顶是较小的那部分中最大的，即第k大。
        例：[1,2,3,4,5]，第3大的是3，所以最大堆要存5-3+1 = 3个元素，即12还要包含第3大的3
    3. QuickSelect

补充：方法一用最小堆的理解
- 如果堆的元素个数小于 k，就可以直接插入堆中。
- 如果堆的元素个数等于 k，则检查堆顶与当前出现次数的大小。如果堆顶更大，说明至少有 k 个数字的出现次数比当前值大，故舍弃当前值；否则，就弹出堆顶，并将当前值插入堆中。
所以最后遍历完后最小堆中剩的就是最大的k个数，最小的堆顶也就是第k大的数！
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
    方法3：Quick Select 霍尔分区法 （采用双指针分区，效率高）    快选记这个！
    首先进行问题转换：
        例如大小为n = 5的数组：[1, 2, 3, 4, 5]
        找第k = 2大的数 -> 找第(5 - 2)小的数 （0-index）
        即找第k大的数相当于找排序后下标为(n - k)的数。
        所以在下标转换后，我们在算法中用的下标，比如返回的j，能直接和转换后的k（k = n - k）进行比较，因为都是0-index了！
    
    重点：和卢默分区的区别
        1. 卢默分区完成一次后，保证了pivot左边的数严格小于pivot，右边的数严格大于pivot，所以pivot的下标就是完整排序后真正的下标。
           所以当返回的下标 == k时，那么返回的pivot_idx就是答案。
        2. 霍尔分区完成一次后，返回j，仅能保证左半部分[left,j] <= pivot，右半部分[j + 1,right] >= pivot，而不能保证下标j处的数
           就在完整排序后的下标j。因为在while循环中，我们把 >= pivot的数往右放， <= pivot的数往左移，没有严格小于或等于，这就造成了
           j不是真实下标。例如，如果数组中有重复的数，且刚好都等于pivot，那么重复数在分区后可能会被分到了左右两边，最后返回的j也就不是真正的下标。
           总结，霍尔分区返回j后，只能保证：[left, j] <= pivot, [j + 1, right] >= pivot
           
    所以，我们得到返回的j时，分两种情况：
        1. k > j:
            我们在 [j + 1, right]找。
                通过个数想（即1-index）：目前左半部分共(j-left+1)个数，我们要找排序后下标为k的数，即要找第k+1个数。
                此时k > j，
                    两边同时+1得到 -> k + 1 > j + 1
                    目前左半部分[left, j]共(j-left+1) = j + 1 - left个数，其中left >= 0
                    则k + 1 > j + 1 >= j + 1 - left
                    最终我们得到k + 1 > j + 1 - left
                说明左区间[left, j]的个数比我们要找的第k+1个数少，所以要找的一定在这个区间右边（即可以直接排除整个[left, j]）。 
                （就算我们要找的数为重复数，在左右区间都存在，那么也能把[left, j]去掉，因为这个重复数在右区间也有，在真正排序后
                下标k也一定大于j！）
        2. k <= j:
            我们在[left, j]找。为什么要包含j呢？
                因为左半部分[left, j] <= pivot，并不像卢默分区后严格小于，所以真正排序后下标k的数也可能就是j。所以我们要把j包含上。
                
    
    补充：为什么下面的写法（把if反过来）不行？
        if k < j:
                return quick_select(left, j - 1, k)
            else:  # k >= j
                return quick_select(j, right, k)
        
        因为，[left, j] <= pivot，如果k < j，并不能排除下标j，因为上面解释过，左半部分没有被真正排序，所以下标j也有可能是
        完整排序后的下标k！
        
    补充：为什么初始化时i = left - 1，j = right + 1，不能写成i = left，j = right？
        如果 nums[left] 就已经是一个不小于 pivot 的值，则第一个 while True 不会执行 i += 1，i 不会移动；
        同理，nums[right] 若已经不大于 pivot，j 也不会减小；
        这就可能导致死循环或逻辑错误，比如当 nums[i] == nums[j] == pivot 时，两个指针根本不移动，而 i < j 条件仍满足，于是会 重复交换同一个位置的值，造成死循环。
        我们希望两个指针即使都等于pivot时也各自更新一次好走出while循环，所以初始化成left-1和right+1这样每次先更新指针再判断，就不会死循环！
    """
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[left]  # 随便选一个pivot，不需要记录index，只看值即可
            i, j = left - 1, right + 1  # 初始化ij双指针，指向当前区间[l,r]的左右两侧，即l - 1和r + 1
            while i < j:
                # i从左往右找第一个 >= pivot的下标
                while True:
                    i += 1
                    if nums[i] >= pivot:
                        break
                # j从右往左找第一个 <= pivot的下标
                while True:
                    j -= 1
                    if nums[j] <= pivot:
                        break
                # 如果此时i < j，则进行交换，使得大的到右边去，小的到左边去
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            # 返回时，j是第一个小于等于pivot的数，所以有[left, j] <= pivot, [j + 1, right] >= pivot。霍尔分区和卢默分区不同的是这里j不一定就是最终排序后正确的下标！
            return j  # 按习惯返回j就行，i的话搞不清invariant，所以记住返回j即可

        def quick_select(left, right):
            if left == right:
                return nums[left]
            j = partition(left, right)
            # 由于霍尔分区返回的j不一定是排序后真正的下标，所以，j == k时nums[k]不一定就是下标k的数！所以我们只能按照[left, j] <= pivot, [j + 1, right] >= pivot这个invariant去做！
            if k > j:  # k > j时能直接排除掉左区间[left, j]，见上面解释
                return quick_select(j + 1, right)
            else:  # k <= j
                return quick_select(left, j)

        n = len(nums)
        k = n - k
        return quick_select(0, n - 1)

    """
    方法4：Quick Select 卢默分区法 (第41个test过不了，因为卢默分区法是单指针遍历，效率低！)
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



"""
补充：求数组中第k小的数
求第k大的数时使用小顶堆存最大的k个数
那么求第k小的时候反着来，使用大顶堆存最小的k个数
"""
class Solution1:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # 最大堆（通过取反实现）
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        # 堆顶是第k小元素的相反数
        return -max_heap[0]