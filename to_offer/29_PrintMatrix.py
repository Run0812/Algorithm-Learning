"""
面试题29：顺序打印矩阵
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次，打印出每一个数字。
例：
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
打印：1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10
"""
def print_matrix(matrix):
    """
    :param matrix:print_matrix
    :return:None
    """
    if not matrix:
        return None
    start = 0
    row = len(matrix)
    col = len(matrix[0])

    while row > start * 2 and col > start * 2:
        # one round
        col_end = col - start - 1
        row_end = row - start - 1
        for j in range(start, col_end+1):
            print(matrix[start][j])
        if row_end > start:
            for i in range(start+1, row_end+1):
                print(matrix[i][col_end])
        if col_end > start and row_end > start:
            for j in range(col_end-1, start-1, -1):
                print(matrix[row_end][j])
        if col_end > start and row_end - 1 > start:
            for i in range(row_end-1,start,-1):
                print(matrix[i][start])
        start += 1
    return

def print_matrix_2(matrix):
    """
    :param matrix: matrix
    :return: print list
    """
    if matrix:
        row = len(matrix)
        col = len(matrix[0])
    else:
        return []
    ans = [] # not necessary just for LeetCode sol
    # O(n) space
    m = range(row)
    # row to print
    n = range(col)
    # col to print
    while True:
        # print row
        ans.extend([matrix[m[0]][y] for y in n])
        # del this row
        m.pop(0)
        # check if print all cols
        if not m:break
        # print col
        ans.extend([matrix[x][n[-1]] for x in m])
        # del this col
        n.pop(-1)
        # check if print all rows
        if not n:break
        # switch to print bottom&left / top&right
        m.reverse()
        n.reverse()
    return ans


m = [[3],[2]]
print_matrix(m)