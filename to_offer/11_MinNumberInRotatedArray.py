"""
面试题11：旋转数组的最小数字
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增序列的数组
的一个旋转，输出旋转数组的最小元素。
例：数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该
数组的最小值为1。
"""

def min_number_in_rotated_array(r_nums):
    """
    :param r_nums:rotated arrat
    :return: min number
    """
    if not r_nums:
        return None
    left = 0
    right = len(r_nums)-1
    while left < right:
        mid = (left + right) // 2
        if r_nums[mid] == r_nums[right] == r_nums[left]:
            right -= 1
        elif r_nums[mid] <= r_nums[right]:
            right = mid
        else:
            left = mid + 1
    return r_nums[left]

print(min_number_in_rotated_array([2,2,0,1,2,2,2]))