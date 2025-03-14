# 274
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # sort in descending order
        """
        我们先把citations从大到小sort一下，因为最大的h值就是len(citations)，
        所以我们从大到小枚举h值,我们取第一个满足条件的h即可，条件：
            从大到小排序的citations里，当前h个citation数量中最后一个>=h,
            说明当前h满足条件。
            因为最后一个是前h个里面最小的，所以它能决定h的最大值，又因为我们是从大到小遍历h，
            所以遇到第一个满足条件的h即返回
        如果便利完都没有满足条件的h，说明所有论文引用都是0，直接返回0即可
        
        从大到小遍历h保证了只要遍历到第一个满足条件的h，直接就可以返回
        如果是从小到大sort citations且h值由小到大遍历，则遍历中citation数量增加但h（余下的len）
        减小，很难去判断到底选当前还是下一个！（当然我们也可以还是从大到小遍历h，但正向遍历从小到大sort的citation！）
        """
        for h in range(len(citations), 0, -1):
            # h是从大到小，citations里需要每次看h个论文里最小的，即从右往左看（h-1）
            if citations[h-1] >= h:
                return h
        return 0

    def hIndex1(self, citations: List[int]) -> int:
        citations.sort()  # 正向sort
        """
        只要h是从大到小遍历即可，然后对应的citations里我们要看当前h个里最小的那个！
        如果从小到大sort citation，即从左到右看，如果从大到小sort，则从右往左看
        都是h从大到小看，citation从小到大看！
        """
        for h in range(len(citations), 0, -1):  # h从大到小
           if citations[len(citations)-h] >= h:
               return h
        return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    #           [6, 5, 3, 1, 0]
    sol = Solution()
    print(sol.hIndex(citations))

