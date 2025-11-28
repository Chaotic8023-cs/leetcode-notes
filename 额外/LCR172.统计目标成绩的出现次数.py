from typing import *


"""
同34题找target的左右边界
找到后只需要右边界-左边界+1即可
"""
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        def leftmost():
            left, right = 0, len(scores)
            while left < right:
                mid = (left + right) >> 1
                if target <= scores[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left if 0 <= left < len(scores) and scores[left] == target else -1

        def rightmost():
            left, right = 0, len(scores)
            while left < right:
                mid = (left + right) >> 1
                if target >= scores[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left - 1 if 0 <= left - 1 < len(scores) and scores[left - 1] == target else -1
        
        lm, rm = leftmost(), rightmost()
        if lm == -1 and rm == -1:  # 找不到target
            return 0
        elif lm == -1 or rm == -1:  # 只找到1个target
            return 1
        else:  # [lm, rm]都是target
            return rm - lm + 1