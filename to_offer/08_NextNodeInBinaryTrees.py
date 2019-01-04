"""
面试题8：二叉树的下一个节点
题目：给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？树中的节点除了
有两个分别指向左、右节点的指针，还有一个指向父节点的指针。
例:
                 a
        |b             c|
    |d      e|       |f     g|
         |h     i|
中序遍历为{d, b, h, e, i, a, f, c, g}
输入b输出h，输入i输出a
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


def next_node_in_binary_trees(cur_n):
    """
    :param cur_n: current node
    :return:inoreder next node
    """
    if not cur_n:
        return 'EMPTY INPUT'
    if cur_n.right:
        next_n = cur_n.right
        while next_n.left:
            next_n = next_n.left
    else:
        if not cur_n.parent:
            return None
        if cur_n.parent.left == cur_n:
            next_n = cur_n.parent
        else:
            next_n = cur_n.parent
            while next_n.parent and next_n.parent.left != next_n:
                next_n = next_n.parent
            else:
                next_n = next_n.parent
    return next_n

root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.parent = root.right.parent = root
# root.left.left = TreeNode('d')
# root.left.right = TreeNode('e')
# root.left.left.parent = root.left.right.parent = root.left
# root.left.right.left = TreeNode('h')
# root.left.right.right = TreeNode('i')
# root.left.right.left.parent = root.left.right.right.parent = root.left.right
# root.right.left = TreeNode('f')
# root.right.right = TreeNode('g')
# root.right.left.parent = root.right.right.parent = root.right

ans = next_node_in_binary_trees(root.right)
print(ans)