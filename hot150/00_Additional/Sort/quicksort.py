from typing import *
import random


def partition(nums, left, right):  # partition array [left, right], in-place
    pivot_idx = random.randint(left, right)
    pivot = nums[pivot_idx]
    # move the pivot to the end
    nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
    # partition the array
    """
    i指针记录了下一个比pivot小的元素应该放置的位置，一开始就是最开头的位置left
    j用来遍历[left,right)，right不用看因为是pivot：
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


def quickSort(nums, left, right):
    if left < right:
        pivot_index = partition(nums, left, right)  # Partition the array
        quickSort(nums, left, pivot_index - 1)      # Sort left part
        quickSort(nums, pivot_index + 1, right)     # Sort right part


if __name__ == '__main__':
    nums = [7, 2, 1, 8, 6, 3, 5, 4]
    quickSort(nums, 0, len(nums)-1)
    print(nums)

