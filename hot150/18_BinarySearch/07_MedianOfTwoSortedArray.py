# 4
from typing import *


class Solution:
    # https://www.bilibili.com/video/BV1Xv411z76J/?share_source=copy_web&vd_source=99743587cb772eab2bb318efc910bdaf
    """
    O(log(m+n))
    思路：确定一个分割线把两个数组分成两部分，则中位数就可以由这个分割线两边的四个数决定
    分割线需满足：
    1. 分完后nums1和nums2总共的左边元素个数和右边相等（m+n为偶数），或左边比右边多1（m+n为奇数）
    2. 分割线左边的元素都小于分割线右边的元素，即nums1分割线左边<=nums2分割线右边 and nums2分割线左边<=nums1分割线右边
    在确定分割线时我们可以用二分查找来找到满足条件的分割线
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 记短的数组为num1，长的为num2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        # 算分割线左边的元素总数
        total_left = (m + n + 1) // 2
        """
        定义分割线：
        在第一个数组nums1中的分割线的右侧第一个元素的index为i，即分割线左边一共i个元素
        在第二个数组nums2中的分割线的右侧第一个元素的index为j，即分割先左边一共有j个元素
        所以：i+j = total_left
        
        找分割线：先找nums1的[0, m]中的分割线i，然后就能通过total_left计算出nums2中的，
        使得nums1中分割线左边的元素小于nums2中分割线右边的元素，同时nums2中分割线左边的元素
        小于nums1中分割线右边的元素，即nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]
        
        下面if else的条件是根据上面分割线的两个条件的左边这个确定的，也可以根据右边的确定，但需要修改边界条件，就不用记了
        """
        left, right = 0, m  # 包含了cut在最左边和最右边的情况，即cut左边和右边都没元素的情况
        while left < right:
            # 一般mid = l+(r-l)//2，但是为了应对left和right挨到一起的情况[left,right] (此时一般mid计算会使得i=left)，+1就能保证mid为right，底下的else中left就能右移而不是不变
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i-1] > nums2[j]:  # 如果nums1的分割线的左边大于nums2的分割线的右边，则nums1分割线需要左移
                # 下一个搜索区间：[left, i-1]
                right = i - 1
            else:
                # 下一个搜索区间：[i, right]
                left = i
        # 出循环时left=right, 此时i，j就是找到的分割线
        i = left
        j = total_left - i
        # 定义挨着分割线的4个数
        """
        控制边界条件，即分割线在最左侧和最右侧：
        对于nums1，如果分割线i为0，则意味着左边没元素了，同时因为左边这个元素要小于nums2右边的数（nums1[i-1] <= nums2[j]），
        我们就把这个不存在的nums1左边的数（nums1[i-1]）设为-inf来满足之后的条件
        对于nums1，如果分割线为m，则意味着右边没元素了，同时因为右边的这个元素需要大于nums2左边的数（nums2[j-1] <= nums1[i]），
        我们就把这个不存在的nums1右边的数（nums1[i]）设为inf来满足之后的条件
        同理，nums2分割线的左右两侧的数值也需这样设置
        """
        nums1LeftMax = -float('inf') if i == 0 else nums1[i-1]      # nums1分割线左边的数
        nums1RightMin = float('inf') if i == m else nums1[i]        # nums1分割线右边的数
        nums2LeftMax = -float('inf') if j == 0 else nums2[j-1]     # nums2分割线左边的数
        nums2RightMin = float('inf') if j == n else nums2[j]        # nums2分割线右边的数
        """
        确定分割线后最终中位数的计算方法
        1. m+n为奇数：分割线左边的最大的那个数（因为odd，左边元素比右边多1，这个多的就是中位数）
        2. m+n为偶数：分割线左边最大数和分割线右边最小的数取平均（恰好就是merged array的中间两个数）
        """
        if (m + n) % 2 == 1:  # odd
            return max(nums1LeftMax, nums2LeftMax)
        else:  # even
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2

    # naive: 直接merge再求中位数, 面试问的话没要求复杂度直接写这个：O(m+n)
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1, nums2):
            result = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1
            if i < len(nums1):
                result += nums1[i:]
            else:
                result += nums2[j:]
            return result

        merged = merge(nums1, nums2)
        mid = (len(merged)-1) // 2  # (left+right) // 2
        if len(merged) % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid+1]) / 2


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(sol.findMedianSortedArrays(nums1, nums2))
