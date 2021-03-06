"""
面试题50：第一个只出现一次的字符
题目1：字符串中第一个只出现一次的字符
在字符串中找到第一个只出现一次的字符。

例:
输入"abaccdeff",则输出'b'。
"""

def first_not_repeating_char(string):
    """
    :param string: string
    :return: first char appear once
    """
    alphabet = {}
    for i in range(len(string)):
        if string[i] in alphabet:
            alphabet[string[i]] = -1
        else:
            alphabet[string[i]] = i
    first = float('INF')
    res = None
    for key in alphabet:
        val = alphabet[key]
        if val != -1 and val < first:
            first = val
            res = key
    return res

print(first_not_repeating_char('google'))