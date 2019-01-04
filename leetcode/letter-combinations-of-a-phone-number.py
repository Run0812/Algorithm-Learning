def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    d = list(digits)
    n_c = {'1': '*', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    already = ['']
    while d:
        comb = []
        num = d.pop(0)
        for s in already:
            for c in n_c[num]:
                comb.append(s + c)
        already = comb
    return comb

digits = '23'
print(letterCombinations(digits))
print()