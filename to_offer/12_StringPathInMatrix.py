"""
面试题12：矩阵中的路径
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一路，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径
经过了矩阵的某一个，那么该路径不能再次进入该格子。例如，在下面的3x4的矩阵中包含一条
字符串"bfce"的路径(路径中的字母用下划线标出)。但矩阵中不包含字符串"abfb"的路径，因
为字符串的第一个字母b占据了矩阵的第一行第二个格子后，路径不能再次进入这个格子。
例：
a b_ t  g
c f_ c_ s
j d  e_ h
"""

def string_path_in_matrix(map, path):
    """
    :param map: puzzle matrix
    :param path: string path
    :return: bool, has path or not
    """

    def search_path(boundary, path, k, cur, pre):
        """
        :param path: path string
        :param k: path progress
        :param cur: current block index
        :param pre: previous passby block list
        :return:
        """
        i ,j = cur
        row, col = boundary
        has_path = False
        if k > len(path)-1:
            return True
        if 0 <= i <= row and 0 <= j <= col:
            if map[i][j] == path[k] and cur not in pre:
                pre.append(cur)
                has_path = search_path(boundary, path, k+1, (i+1,j), pre)\
                        or search_path(boundary, path, k+1, (i,j+1), pre)\
                        or search_path(boundary, path, k+1, (i-1,j), pre)\
                        or search_path(boundary, path, k+1, (i,j-1), pre)
        return has_path

    if map and map[0] and path:
        # empty input check
        row = len(map) - 1
        col = len(map[0])
        boundary = (row, col)
    else:
        raise Exception('EMPTY INPUT')
    cur = None
    for i in range(row):
        for j in range(col):
            # start block search
            if path[0] == map[i][j]:
                cur = (i,j)
                break
    if not cur:
        # not in map
        return False
    return search_path(boundary, path, 0, cur, [])

print(string_path_in_matrix([['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']],'abtg'))