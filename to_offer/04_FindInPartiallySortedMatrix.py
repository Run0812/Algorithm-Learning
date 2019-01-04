"""
面试题4：二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序，每一列都按照从上到下递增的顺序
排序。每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
整数，判断数组中是否含有该整数。
例：
1  2  8  9
2  4  9  12
4  7  10 13
6  8  11 15
查找7，输出True；查找5，输出False
"""
def find_in_partially_sorted_matrix(nums, target):
    """
    :param nums: the matrix
    :param target: num for searching
    :return: find or not or empty input
    """
    if not nums or not nums[0]:
        # empty input
        return None
    row = len(nums) - 1
    col = len(nums[0]) - 1
    i,j = 0, col
    find = False
    while i <= row and j >= 0:
        if  target == nums[i][j]:
            find = True
            break
        elif target > nums[i][j]:
            i += 1
        else:
            j -= 1
    return find

nums = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
nums2 = [[]]
target = 22
print(find_in_partially_sorted_matrix(nums2,target))