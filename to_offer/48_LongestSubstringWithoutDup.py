"""
面试题48：最长不包含重复字符的子字符串
题目：请从字符串中找到一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
假设该字符串只包含'a'~'z'的字符。
例：
在字符串'arabcacfr'中，最长的不包含重复字符的子字符串是"acfr"，长度为4。
"""

def longest_sub_str_without_dup(string):
    """
    :param string: string
    :return: max length of substr with out duplication
    """
    cur_len = 0
    max_len = 0
    last_pos = [-1] * 26
    for i in range(len(string)):
        curchr_pos_i = ord(string[i]) - ord('a')
        cur_chr_pre_i = last_pos[curchr_pos_i]
        if i - cur_len >cur_chr_pre_i:
            cur_len += 1
        else:
            cur_len = i - cur_chr_pre_i
        max_len = max(max_len, cur_len)
        last_pos[curchr_pos_i] = i
    return max_len

print(longest_sub_str_without_dup(""))