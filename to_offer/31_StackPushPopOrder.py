"""
面试题31：栈的压入、弹出序列
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的
弹出顺序。假设压入栈的所有数字均不相等。
例：
序列{1, 2, 3, 4, 5}是一个压栈序列，{4, 5, 3, 2, 1}是该压栈序列的对应的一个弹
出序列，但{4, 3, 5, 1, 2}就不可能是该压栈序列的弹出序列。
"""

def stack_push_pop_order(push_ord, pop_ord):
    """
    :param push_ord:push sequence
    :param pop_ord: pop sequence
    :return: bool
    """
    stack = []
    while pop_ord:
        while not stack or stack[-1] != pop_ord[0]:
            if not push_ord:
                return False
            stack.append(push_ord.pop(0))
        stack.pop()
        pop_ord.pop(0)
    return True

push =[0,1,2,3,4,5]
pop = [4,5,3,2,1]
print(stack_push_pop_order(push, pop))