'''
面试题3：数组中重复的数字
题目1：找出数组中重复的数字
在一个长度为n的数组里中所有数字都在0 ~ n-1的范围内。请找出数组中任意一个重复的数字。
例：[2, 3, 1, 0, 2, 5, 3] 输出 2 或者 3。
'''


def duplication_in_array(nums):
    '''
    :param nums: list to check
    :return: duplicated num or None
    '''
    dup_num = None
    for i, num in enumerate(nums):
        if num < 0 or num > len(nums) - 1:
            # boundary
            dup_num = num
            break
        while num != i:
            # hash func: i(key) = num(value)
            if nums[num] == num:
                # collision
                dup_num = num
                break
            else:
                # swap -> store num in hash way
                nums[num], nums[i] = num, nums[num]
    return dup_num

print(duplication_in_array([2,3,1,0,2,5,3]))

