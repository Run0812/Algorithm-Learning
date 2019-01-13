"""
面试题32：从上到下打印二叉树
题目3：之字形打印二叉树
请实现一个函数按照之字形顺序打印二叉树，即第一行按照哦从左到右的顺序打印，
第二层按照啊从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此
类推。
例：
输入：
                1
            /        \
           2          3
         /   \     /     \
        4    5     6     7
       / \  / \   / \   / \
      8  9 10 11 12 13 14 15
输出：
1
3 2
4 5 6 7
15 14 13 12 11 10 9 8
"""

def print_tree_lines(root):
    layer = [root]
    next_layer = []
    reverse = -1
    while layer:
        for node in layer:
            if node:
                print(node.val, end = " ")
                next_layer.extend([node.left, node.right][::-reverse])
        print()
        layer = next_layer[::-1]
        next_layer = []
        reverse = -reverse
    return

from datstru import list_to_treenode

root = list_to_treenode(list(range(1,32)))
print_tree_lines(root)