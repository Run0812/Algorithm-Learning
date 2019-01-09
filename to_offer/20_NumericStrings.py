"""
面试题20：表示数值的字符串
题目：请实现一个函数来判断字符串是否表示数值（包括整数和小数）。
例：
字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"、"12e+5.4"都不是。
"""

def numeric_strings(s):
    """
    :param s: num string
    :return: is num
    """

    def is_num(s, allow_dot = True, allow_E = True):
        """
        :param s: num string
        :param allow_dot: if allow .
        :param allow_E: if allow E/e
        :return: Bool
        """
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sign = ['+', '-']
        if s[0] in sign:
            i = 1
        else:
            i = 0
        while i < len(s):
            str = s[i]
            if str in number:
                pass
            elif str == '.' and allow_dot:
                return is_num(s[i+1:], allow_dot = False)
            elif str in ['e', 'E'] and allow_E and i + 1 < len(s):
                return is_num(s[i+1:], allow_dot = False, allow_E = False)
            else:
                return False
            i += 1
        return True

    return is_num(s)

strings = '.123E1'
print(numeric_strings(strings))