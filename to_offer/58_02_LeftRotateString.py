"""
面试题58:翻转字符串
题目2：左旋转字符串
字符串左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个
函数实现字符串左旋转操作的功能。

例：
输入："abcdefg", 2
输出："cdefgab"
"""


def left_rotate_string(s, k):

    def reverse(string, start, end):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
        return
    if k < 0:
        raise Exception('Invalid K')
    string = list(s)
    reverse(string, 0, k-1)
    reverse(string, k, len(string)-1)
    reverse(string, 0, len(string) - 1)

    return ''.join(string)

print(left_rotate_string('', -2))