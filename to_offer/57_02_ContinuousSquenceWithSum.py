"""
面试题57：和为s的数字
题目2:和为s的连续正数序列
输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。

例：
输入15，由于1 + 2 + 3 + 4 + 5 = 4 + 5 + 6 = 7 + 8 = 15，
所以打印出3个连续序列1~5、4~6和7~8。
"""


def continuous_sequence_with_sum(s):
    """
    :param s: target sum
    :return: None
    """
    small, big = 1, 2
    sum = 3
    while small <= (1+s) // 2:
        if sum == s:
            print(list(range(small, big + 1)))
            sum -= small
            small += 1
            big += 1
            sum += big
        elif sum > s:
            sum -= small
            small += 1
        else:
            big += 1
            sum += big
    return

continuous_sequence_with_sum(15)