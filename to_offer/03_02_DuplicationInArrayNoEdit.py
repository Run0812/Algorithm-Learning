'''
面试题3：数组中重复的数字
题目2：不修改数组找出数组中重复的数字
在一个长度为n+1的数组中，所有数字都在 1 ~ n的范围中，所以数组中至少有一个数字是重复的。
请找出任意一个重复的数字，但不能修改输入的数组。
例：[2, 3, 5, 4, 3, 2, 6, 7] 输出 2 或者 3
'''

def duplication_in_array_no_edit(nums):
    """
    :param nums: list to search
    :return: duplicated num
    """
    import collections
    dup_num = None
    count = collections.Counter(nums)
    for num in count:
        if count[num] > 1:
            dup_num = num
            break
    return dup_num

# print(duplication_in_array_no_edit([4, 2, 4, 4, 3, 2, 6, 7]))

def duplication_i_array_no_edit2(nums):
    """
    :param nums: list to search
    :return: duplicated num
    """
    if not nums:
        return None
    n_min = 1
    n_max = len(nums)-1
    while n_min <= n_max:
        mid = (n_min + n_max) // 2
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        if n_min == n_max:
            # no duplication check
            dup_num = mid if count > mid else None
            break
        if count > mid:
            n_max = mid
        else:
            n_min = mid + 1
    return dup_num

print(duplication_i_array_no_edit2([1, 2, 3, 4, 5, 6, 7, 8]))
