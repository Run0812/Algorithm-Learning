"""
面试题10：斐波那契数列
题目1：求斐波那契数列的第n项。
例：输入10 输出55
"""

def fibonacci_recursion(n):
    """
    :param n: F(n)
    :return: val
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_loop(n):
    """
    :param n: F(n)
    :return: val
    """
    if n == 0:
        return 0
    cache = [0,1]
    for i in range(n-2):
        cache[0],cache[1] =cache[1], cache[0] + cache[1]
    return cache[0] + cache[1]

def fibonacci_matrix_mul(n):
    """
    :param n: F(n)
    :return: val
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    mul = [[0,1],[1,1]]
    def matrix_mul(matrix1, matrix2):
        """
        :param matrix1:2*2 matrix
        :param matrix2: 2*2 matrix
        :return: 2*2 matrix
        """
        (a11, a12), (a21, a22) = matrix1
        (b11, b12), (b21, b22) = matrix2
        c11 = a11 * b11 + a12 * b21
        c12 = a11 * b12 + a12 * b22
        c21 = a21 * b11 + a22 * b21
        c22 = a21 * b12 + a22 * b22
        mul_matrix =[[c11, c12], [c21, c22]]
        return mul_matrix

    def matrix_pow(mul,n):
        """
        :param mul:2*2 matrix
        :param n: pow n
        :return: 2*2 matrix
        """
        if n == 1:
            return mul
        if n == 2:
            return matrix_mul(mul, mul)
        temp = matrix_pow(mul, n // 2)
        pow = matrix_mul(temp, temp)
        if n % 2:
            return matrix_mul(pow, mul)
        else:
            return pow

    return matrix_pow(mul, n-1)[1][1]

# print(fibonacci_loop(1000000))
# print(fibonacci_matrix_mul(1000000))