
def re_exp_matching_backward(s, p):
    """
    :type s: str for match
    :type p: pattern str
    :rtype: match or not
    """
    if not s or not p:
        raise Exception('Empty Input')

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

    if not s or not p:
        raise Exception('Empty Input')

    return is_match(0,0)


def re_exp_matching_dp(s, p):

    return

s = "aa"

p = "a"
print(re_exp_matching(s,p))