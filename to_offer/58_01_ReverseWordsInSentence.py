"""
面试题58：翻转字符串
题目1：反转单词顺序
输入一个英文句子，翻转句子中的单词顺序，但单词内字符顺序不变。为简单器件，标点符号和普通字母一样处理。

例：
输入："I am a student."
输出："student. a am I"
"""


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    return ' '.join(words[::-1])

# print(reverseWords("I am a student."))

def reverse_word_in_sentence(s):

    def reverse(string, start, end):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
        return

    string = list(s)
    reverse(string, 0 , len(string)-1)
    word_head = 0
    for i in range(len(string)):
        str = string[i]
        if str == ' ':
            reverse(string, word_head, i-1)
            word_head = i + 1
    reverse(string, word_head, len(string)-1)
    return ''.join(string)

print(reverse_word_in_sentence("Im am a student."))