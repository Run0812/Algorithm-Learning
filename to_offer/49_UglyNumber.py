"""
面试题49：丑数
题目：我们把只包含因子2、3和5的数称为丑数。求按从小到大的顺序的第1500个丑数。
例：
6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当作第一个丑数。
"""

def get_ugly_num(index):
    """
    :param index:the index of required ugly number
    :return: ith ugly number
    """
    ugly_num = [1]
    i_2 = i_3 = i_5 =0
    while len(ugly_num) < index:
        ugly_num.append(min(ugly_num[i_2] * 2, ugly_num[i_3] * 3, ugly_num[i_5] * 5))
        while ugly_num[i_2] * 2 <= ugly_num[-1]:
            i_2 += 1
        while ugly_num[i_3] * 3 <= ugly_num[-1]:
            i_3 += 1
        while ugly_num[i_5] * 5 <= ugly_num[-1]:
            i_5 += 1
    return ugly_num[-1]

print(get_ugly_num(100))