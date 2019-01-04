s = '  -43'


def myAtoi(s):
    """
    :type str: str
    :rtype: int
    """
    s = s.lstrip()
    if not s:
        return 0
    sample = ''
    if s[0] == '-' or s[0] == '+':
        sample = s[0]
        s = s[1:]
    end = len(s)

    for i, char in enumerate(s):
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            end = i + 1
            break
    num = s[:end]
    print('num', num)
    if num:
        num = -int(num) if sample == '-' else int(num)
        if num.bit_length() <= 32:
            return num
        else:
            if sample == '-':
                return 'INT_MIN(-2 ** 31)'
            else:
                return 'INT_MAX(2 ** 31 - 1)'
    return 0

myAtoi(s)