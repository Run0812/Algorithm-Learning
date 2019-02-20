"""
面试题53：在排序数组中查找数字
题目1：数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。

例：
输入数组{1, 2, 3, 3, 3, 3, 4, 5}和数字3。
由于3在这个数组中出现了4次，输出4。
"""

def num_of_k(nums, k):
    """
    :param nums: array
    :param k: find K
    :return: times that K appears
    """
    # find middle k
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] > k:
            right = mid - 1
        else:
            break
    else:
        raise Exception('NO SUCH NUMBER')
    start_l, start_r = left, mid
    end_l, end_r = mid, right
    # find start boundary
    while start_l <= start_r:
        start = (start_l + start_r) // 2
        if nums[start] != k:
            start_l = start + 1
        else:
            if start > 0 and nums[start - 1] == k:
                start_r = start - 1
            else:
                break
    # find end boundary
    while end_l <= end_r:
        end = (end_l + end_r) // 2
        if nums[end] != k:
            end_r = end - 1
        else:
            if end + 1 < len(nums) and nums[end + 1] == k:
                end_l = end + 1
            else:
                break

    return end - start + 1

nums = [1]
k = 5
print(num_of_k(nums , k))