"""
面试题13：机器人的运动范围
题目：地上有一个m行n列的方格。一个机器人从坐标(0,0)的格子开始移动，他每次可以向左、
右、上、下移动一格，但不能进入行坐标和列坐标的数位之和大于k的格子。
例:当k为18时，机器人能够进入(35, 37)，因为3+5+3+7=18。但它不能进入放个(35, 38)，
因为3+5+3+8=19。请问该机器人能够到达多少个格子?
"""

def robot_move(row, col, k):
    """
    :param row: row of matrix, m
    :param col: col of matrix, n
    :param k: bit sum limit
    :return: num of blocks can reach
    """
    def bit_sum(num):
        """
        calculate bit sum
        :param num: num
        :return: bit sum
        """
        b_sum = 0
        while num:
            b_sum += num % 10
            num = num // 10
        return b_sum

    if row < 1 or col < 1:
        raise Exception('Invalid Matrix')

    to_check = [(0,0)]
    next_check = set()
    block_count = 0
    while to_check:
        i_cur, j_cur = to_check.pop(0)
        block_count += 1
        if j_cur + 1 < col and bit_sum(i_cur) + bit_sum(j_cur + 1) <= k:
            next_check.add((i_cur, j_cur+1))
        if i_cur + 1 < row and bit_sum(i_cur + 1) + bit_sum(j_cur) <= k:
            next_check.add((i_cur + 1, j_cur))
        if not to_check:
            to_check.extend(list(next_check))
            next_check = set()
    return block_count

b = robot_move(1,5,0)
print(b)