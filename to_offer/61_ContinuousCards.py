"""
面试题61：扑克牌中的顺子
题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即5张牌是不是连续的。
2~10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
"""


def continuous_cards(cards):
    """
    :param cards: list represents cards
    :return: is continuous
    """
    cards.sort()
    joker = 0
    for card in cards:
        if card == 0:
            joker += 1
        else:
            break
    if joker > 2:
        raise Exception('impossible combo')
    for i in range(joker+1,5):
        if cards[i] - cards[i - 1] != 1:
            joker -= (cards[i] - cards[i - 1] - 1)
        if joker < 0:
            return False
    return True

print(continuous_cards([ 1, 2, 3, 5, 0]))