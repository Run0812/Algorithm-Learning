"""
面试题15:二进制中1的个数
题目：实现一个函数，输入一个整数，输出该数二级制表示中1的个数。
例：
把9表示成二进制是1001，有2位是1。因此如果输入9，则该函数输出2。
"""

def num_of_1_in_b(num):
    """
    due to number in Python3 has no bit limit
    so flag << 1 will never equals 0
    :param num:num
    :return:num of 1 in bin(num)
    """
    flag = 1
    count = 0
    for i in range(num.bit_length()):
        if flag & num:
            count += 1
        flag <<= 1
    return count

def num_of_1_in_b_2(num):
    count = 0
    # will not work if num.bit_length() > 32
    # if num < 0:
    #     num = num & 0xffffffff
    while num:
        num = (num - 1) & num
        count += 1
    return count


print(num_of_1_in_b(-110000000000000000000000),bin(-11000000000000000000000))