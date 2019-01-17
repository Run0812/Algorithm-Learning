"""
面试题37:序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树

例：
树：
        1
       / \
      2   3
     /   / \
    4   5   6
序列化：
[1, 2, 4, $, $, $, 3, 5, $, $, 6, $, $]
"""

from datstru import TreeNode
from datstru import list_to_treenode

def serialize(root):
    """
    :param root:tree root
    :return:pre-order val list
    """
    def preorder(root):
        if not root:
            seq.append('$')
            return
        seq.append(root.val)
        preorder(root.left)
        preorder(root.right)
        return seq
    seq = []
    preorder(root)
    return seq


def deserialize(sequence):
    """
    :param sequence:pre-order val list
    :return: tree root
    """
    def rebuild(seqence, i):
        val = seqence[i]
        if val == '$':
            return None
        root = TreeNode(val)
        root.left = rebuild(seqence, i+1)
        root.right = rebuild(seqence, i+2)
        return root

    if not sequence:
        return None
    return rebuild(sequence, 0)


root = list_to_treenode([1, 2, 3, 4, 'null', 5, 6])
seq = serialize(root)
tree = deserialize(seq)
print(seq)
