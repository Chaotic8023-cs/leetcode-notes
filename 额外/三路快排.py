"""
三路快排：把数组划分成3部分：<pivot，==pivot，>pivot
思路和#75颜色分类一样
"""
def three_way_partition(nums, pivot):
    i, j = -1, len(nums)
    k = 0
    while k < j:
        if nums[k] < pivot:
            nums[k], nums[i + 1] = nums[i + 1], nums[k]
            i += 1
            k += 1
        elif nums[k] > pivot:
            nums[k], nums[j - 1] = nums[j - 1], nums[k]
            j -= 1
        else:
            k += 1


nums = [3, 5, 2, 1, 4, 2, 3, 5, 2]
pivot = 3
three_way_partition(nums, pivot)
print(nums)


