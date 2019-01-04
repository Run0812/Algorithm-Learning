"""
面试题5：替换空格
题目：实现一个函数把字符串中的每个空格替换成"%20"。
例：输入"We are happy.",则输出"We%20are%20happy."
"""

def replace_spaces(s):
    """
    :param s: original string
    :return: string without space
    """
    new_s = s.replace(' ', '%20')
    return new_s

def replace_space2(string):
    """
    :param string: list of string
    :return: None replace in situ
    """
    n_space = 0
    l = len(string) - 1
    for s in string:
        if s== ' ':
            n_space += 1
    string.extend([0 for _ in range(2*n_space)])
    write = l + 2*n_space
    # write = -1
    scan = l
    while scan >= 0:
        if string[scan] == ' ':
            string[write-2:write+1] = ['%','2','0']
            write -= 3
        else:
            string[write] = string[scan]
            write -= 1
        scan -= 1
    return

a =list("    ")
replace_space2(a)
print(a)
