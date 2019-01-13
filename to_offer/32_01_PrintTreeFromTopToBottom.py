"""
面试题32：从上到下打印二叉树
题目1：不分行从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点，按照从左到右的顺序打印。
例：
输入：
            8
           / \
          6  10
         / \ / \
        5  7 9 11
输出：8, 6, 10, 5, 7, 9, 11
"""

def print_top_to_bottom(root):
    """
    :param root: tree root
    :return: None
    """
    to_print = [root]
    while to_print:
        node = to_print.pop(0)
        if node:
            print(node.val)
            to_print.extend([node.left, node.right])
    return