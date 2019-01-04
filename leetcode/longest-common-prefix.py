def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    i = 0
    while i < min(len(strs[0]), len(strs[1])) and strs[0][i] == strs[1][i]:
        i += 1
    if i == 0:
        return ""
    comstr = strs[0][:i]
    print(i,comstr)
    for str in strs:
        if str[:i] == comstr:
            pass
        else:
            if len(str) < i:
                i = len(str)
            while i > 0 and str[i-1] != comstr[i-1]:
                print(i)
                i -= 1
            if i > 0:
                comstr = comstr[:i]
            else:
                comstr = ""
                break
    print(comstr)
    return comstr

strs = ["flower","flow","fl"]
longestCommonPrefix(strs)