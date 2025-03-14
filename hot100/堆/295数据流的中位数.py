from typing import *
import heapq


"""
用小顶堆（minQ）存较大的一部分数，用大顶堆存较小的一部分数（因为median在中间，所以我们要的是较大一部分的最小的和较小一部分最大的）。我们需要
确保minQ中的元素一直是大于maxQ中的元素，这样才能正确的把所有元素划分成两半，从而正确找到中位数。
我们一直确保：
    1. 要么minQ的元素个数等于maxQ的元素个数（即总数为偶数） -> median = 两个堆顶元素相加除以二，因为此时总数为偶数，两个堆顶元素就是中间的两个
    2. 要么minQ的元素个数比maxQ多1个 -> median = minQ堆顶的元素，因为此时总数是奇数且minQ比maxQ多一，所以中间的数就是大的那部分数中最小的
对于addNum的实现：
如何确保：
    1. minQ的元素一直大于maxQ的元素：
        我们先往maxQ中加，然后再从maxQ弹出一个加入到minQ中。这样做因为先往maxQ中加的话，如果加入的num最终应该在较大的那部分，那就说明
        它比maxQ的所有元素都要大，此时num就会在maxQ的堆顶，弹出的话正好是num。即我们先放到较小的那部分中，如果它比所有较小的数都大，那么就会
        被移动到较大的那部分；如果它比较小的那部分最大的数小，那么较小的那部分的最大的数就会移动到较大部分。这样保证了maxQ一直比minQ的元素要小。
        (即每次把最大的从maxQ移动到minQ中，保证了minQ一直大于maxQ的元素)
        
        能不能先加入到minQ？不能，因为如果加入的num比maxQ的堆顶小，说明它应该到较小的那部分（maxQ）中，但此时先插入到minQ中不能保证插入后
        就是较大的这部分中最小的，即不能保证到堆顶，也就是说它可能就会存在于minQ中，也就破坏了minQ一直大于maxQ元素的限制！
        
    2. minQ元素个数要么等于maxQ，要么比maxQ大1：
        在我们先插入maxQ，再从maxQ弹出一个加入到minQ后，我们检查此时minQ的元素个数是否比maxQ多1个以上，如果是则往回还一个即可。

"""
class MedianFinder:

    def __init__(self):
        self.min_heap = []  # 存较大的元素
        self.max_heap = []  # 存较小的元素

    def addNum(self, num: int) -> None:
        # 先插入小的那部分（maxQ），在从较小的那部分弹出一个放到较大的那部分，确保了minQ的元素一直比maxQ大
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap) + 1:  # 如果总数为奇数，则minQ始终要比maxQ多一个，所以检查一下，如果多1个以上就还一个
            heapq.heappush(self.max_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap) + 1:  # 总数为奇数，此时median = 较大的那部分的堆顶，因为较大的那部分（minQ）元素多1个，minQ的堆顶就是较大那部分最小的，即刚好就是中间那个数
            return self.min_heap[0]
        else:  # len(self.minQ) == len(self.maxQ)：总数为偶数，此时median = 两个堆顶元素求平均，即中间两个数求平均
            return (self.min_heap[0] + (-self.max_heap[0])) / 2  # maxQ存的是负数（因为heapq默认是小顶堆），所以要取反一下






