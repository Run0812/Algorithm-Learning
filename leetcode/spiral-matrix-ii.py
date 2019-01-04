def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    ans = [[0 for i in range(n)] for j in range(n)]
    # i = j = 0
    # blow = 0
    # bhigh = n-1
    # for num in range(1, n ** 2 +1):
    #     ans[i][j] = num
    #     if j < bhigh and i == blow:
    #         j += 1
    #         continue
    #     if i < bhigh and j == bhigh:
    #         i += 1
    #         continue
    #     if j > blow and i == bhigh:
    #         j -= 1
    #         if j == blow:
    #             blow += 1
    #         continue
    #     if i > blow and j == blow-1:
    #         i -= 1
    #         if i == blow:
    #             bhigh -= 1
    #         continue
    row = list(range(n))
    col = list(range(n))
    num = 1
    while row or col:
        for j in col:
            ans[row[0]][j] = num
            num += 1
        row.pop(0)
        for i in row:
            ans[i][col[-1]] = num
            num += 1
        col.pop(-1)
        col.reverse()
        row.reverse()
    return ans

print(generateMatrix(10))
print()