"""
面试题38：字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。

例：
输入：'abc'
输出：'abc', 'acb', 'bac', 'cab', 'cba'
"""

def string_permutation(string):
    """
    :param string:string
    :return: permutation list
    """
    def recursion_core(pre_s, string):
        """
        :param pre_s: n-1 sol
        :param string: str waiting to add
        :return: n sol
        """
        if not string:
            ans.append(pre_s)
            return
        for s in range(len(string)):
            recursion_core(pre_s + string[s], string[:s]+string[s+1:])
    ans = []
    recursion_core('', string)
    return ans

def string_permutation_2(string):
    """
    :param string: string
    :return: permutation list
    """
    def recursion_core(string, start):
        """
        :param string: total string
        :param start: all permutation of string[start:]
        :return:
        """
        if start == len(string):
            comb.append(''.join(string))
        else:
            for i in range(start,len(string)):
                string[i], string[start] = string[start], string[i]
                recursion_core(string, start+1)
                string[i], string[start] = string[start], string[i]
    comb = []
    recursion_core(list(string), 0)
    return comb


print(string_permutation_2('123'))