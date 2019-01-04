"""
面试题17：打印1到最大的n位数
题目：输入数字你，按顺序打印出从1到最大的n位十进制数。
例：
输入3，则打印出1、2、3、...、999。
"""

def print_1_max_of_n_digit(n):
    if n <= 0:
        raise Exception('Invalid Input')
    for i in range(1,10**n):
        print(i)
    return

def list_print(num_in_list):
    """
    print list sequentially
    :param num_in_list: the list stores num in digits
    :return: None
    """
    start = False
    for bit in num_in_list:
        if bit:
            start = True
        if start:
            print(bit, end='')
    print()
    return

def print_1_max_of_n_digit_list(n):
    """
    :param n:num of digit
    :return:None
    """
    if n <= 0:
        raise Exception('Invalid Input')
    cur_num = [0] * n
    while cur_num[0] < 10:
        # 加10次
        for i in range(10):
            list_print(cur_num)
            cur_num[-1] += 1
        # 进位
        for i in range(n-1, 0,-1):
            if cur_num[i] >= 10:
                cur_num[i] = 0
                cur_num[i-1] += 1
            else:
                break

    return

def print_1_max_of_n_digit_list_recursively(n):
    cur_num = [0] * n

    def recursive_print(d_i):
        if d_i == n:
            list_print(cur_num)
            return
        for i in range(10):
            cur_num[d_i] = i
            recursive_print(d_i+1)

        return

    return recursive_print(0)

print_1_max_of_n_digit_list_recursively(3)