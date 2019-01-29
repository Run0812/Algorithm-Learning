"""
面试题47：礼物的最大价值
题目：在一个m x n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或者下移动一格，直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物。

例：
1   10  3   8
12  2   9   6
5   7   4   11
3   7   16  5
最大价值53，1->12->5->7->7->16->5
"""

def max_val_of_gifts(board):
    """
    :param board: gift val board
    :return: max val of gifts
    """
    if not board:
        return 0
    row = len(board)
    col = len(board[0])
    cache = [0] * col
    for i in range(row):
        for j in range(col):
            if j == 0:
                cache[j] = cache[j] + board[i][j]
            else:
                cache[j] = max(cache[j], cache[j-1]) + board[i][j]
    return cache[-1]

board = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
print(max_val_of_gifts(board))