"""
面试题28：对称的二叉树
题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么他是对称的。
例：
对称
    1
   / \
  2   2
 / \ / \
3  4 4  3
不对称
    1
   / \
  2   2
   \   \
   3    3
"""



def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    layer = [root, root]
    while layer:
        left = layer.pop(0)
        right = layer.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val == right.val:
            layer.extend([left.left, right.right, left.right, right.left])
        else:
            return False
    return True


def is_symmetrical(root):
    """
    :param root: root
    :return: bool
    """

    def re_core(preorder, symm_preoder):
        if not preorder and not symm_preoder:
            return True
        if not preorder or not symm_preoder:
            return False
        if preorder.val == symm_preoder.val:
            return re_core(preorder.left, symm_preoder.right) and re_core(preorder.right, symm_preoder.left)

    return re_core(root, root)