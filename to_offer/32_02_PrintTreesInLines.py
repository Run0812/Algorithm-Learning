"""
面试题32：从上到下打印二叉树
题目2：分行从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点，按照从左到右的顺序打印。
每一层打印到一行。
例：
输入：
            8
           / \
          6  10
         / \ / \
        5  7 9 11
输出：
8
6 10
5 7 9 11
"""

def print_tree_lines(root):
    layer = [root]
    next_layer = []
    while layer:
        for node in layer:
            if node:
                print(node.val, end = " ")
                next_layer.extend([node.left, node.right])
        print()
        layer = next_layer
        next_layer = []
    return


from datstru import TreeNode
from datstru import list_to_treenode

root = list_to_treenode([8,6,10,5,7,9,11])
print_tree_lines(root)