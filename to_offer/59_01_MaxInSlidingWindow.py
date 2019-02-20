"""
面试题59：队列的最大值
题目1：滑动窗口的最大值
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。

例：
输入：[2, 3, 4, 2, 6, 2, 5, 1], 滑动窗口大小3
输出：[4, 4, 6, 6, 6, 5]
"""


def max_in_sliding_window(array, window_width):
    """
    :param array: numbers
    :param window_width:sliding window size
    :return: all max number
    """
    if not array or window_width < 1:
        return None
    max_i = []
    res = []
    for i in range(len(array)):
        while max_i and array[i] >= array[max_i[-1]]:
            max_i.pop()
        max_i.append(i)
        while max_i and i - max_i[0] >= window_width:
            max_i.pop(0)
        if window_width - 1 <= i:
            res.append(array[max_i[0]])
    return res

array = [1, 3, 5, 7, 9, 11, 13, 15  ]
size = 4
print(max_in_sliding_window(array, size))
print()