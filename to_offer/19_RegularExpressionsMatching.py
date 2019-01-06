"""
面试题19：正则表达式匹配
题目：请实现一个函数来匹配包含'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符
可以出现任意次（含0次）。在本题中，匹配是指字符串中的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和“ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
"""
def re_exp_matching_backward(s, p):
    """
    :type s: str for match
    :type p: pattern str
    :rtype: match or not
    """
    def is_match(chr_for_match, match_pattern):
        return match_pattern == '.' or match_pattern == chr_for_match

    def match_core(str, pattern):
        if pattern < 0:
            return str < 0
        if str < 0 :
            if p[pattern] != '*':
                return False
            else:
                return match_core(str, pattern - 2)
        if p[pattern] == '*':
            if is_match(s[str], p[pattern - 1]):
                if match_core(str - 1, pattern):
                    return True
            return match_core(str, pattern - 2)
        if is_match(s[str], p[pattern]):
            return match_core(str - 1, pattern - 1)
        return False

    return match_core(len(s) - 1, len(p) -1)


def re_exp_matching(s, p):

    def is_match(str, pattern):
        if str >= len(s) and pattern >= len(p):
            return True
        if str < len(s) and pattern >= len(p):
            return False
        if pattern + 1 < len(p) and p[pattern + 1] == '*':
            if str < len(s) and (p[pattern] == s[str] or p[pattern] == '.'):
                return is_match(str + 1, pattern + 2) or is_match(str + 1, pattern) or is_match(str, pattern + 2)
                # move to 1.next pattern 2. current pattern 3. match 0 time
            else:
                return is_match(str, pattern + 2)
        elif str < len(s) and (s[str] == p[pattern] or p[pattern] == '.'):
            return is_match(str + 1, pattern + 1)
        return False
    return is_match(0,0)


def re_exp_matching_dp(s, p):

    col, row = len(p), len(s)
    dp = [[0]* (col+1) for _ in range(row+1)]
    dp[0][0] = 1
    for i in range(2, col+1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-2]

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if p[j-1] == '*':
                if s[i-1] != p[j-2] and p[j-2] != '.':
                    dp[i][j] = dp[i][j-2]
                elif s[i-1] == p[j-2] or p[j-2] == '.':
                    dp[i][j] = dp[i][j-2] or dp[i-1][j]
            elif s[i-1] == p[j-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]

    return dp[-1][-1] == 1

s = "ab"

p = ".*"
print(re_exp_matching_dp(s,p))