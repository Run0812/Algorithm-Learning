"""
面试题7:重建二叉树
题目:输入某二叉树的前序遍历和中序遍历的结果,请重建该二叉树。假设输入的前序遍历和中序
遍历都不含重复的数字。例如，输入前序遍历序列{1, 2, 4, 7, 3, 5, 6, 8};中序遍历序列
{4, 7, 2, 1, 5, 3, 8, 6}，则重建为下面的二叉树，并返回根节点。
         1
    |2       3|
|4        |5    6|
    7|        |8
"""
from datstru import TreeNode


def construct_binary_tree(preorder, inorder):
    """
    more space need but simple coding
    :param preorder:preorder traversal printout
    :param inorder:inorder traversal printout
    :return:root
    """
    def construct_recursion(preorder, inorder):
        if not preorder:
               return None
        root = TreeNode(preorder[0])
        if preorder[0] in inorder:
            # preorder not match inorder
            i = inorder.index(preorder[0])
        else:
            # print('This is not a binary tree!')
            nonlocal match_flag
            match_flag = False
            return None
        root.left = construct_recursion(preorder[1:i+1],inorder[:i])
        root.right = construct_recursion(preorder[i+1:], inorder[i+1:])
        return root
    if preorder:
        # empty input
        match_flag = True
        root = construct_recursion(preorder, inorder)
        return root if match_flag else print('Invalid Input')
    else:
        return print('EMPTY INPUT')


def construct_binary_tree2(preorder, inorder):
    """
    do not trans new list
    :param preorder: preorder traversal printout
    :param inorder: inorder traversal printout
    :param left: left index of list of this child tree
    :param right: right index of this child tree
    :return: root
    """
    def construct_recursion(preorder, l_pre, r_pre, inorder, l_in, r_in):
        """
        :param preorder: preorder of binary tree
        :param l_pre: start index of subtree's preorder
        :param r_pre: end index of subtree's preorder
        :param inorder: inorder of binary tree
        :param l_in: start index of subtree's inorder
        :param r_in: end index of subtree's inorder
        :return: current node
        """

        if l_pre == r_pre:
            # single node & end recursion
            return TreeNode(preorder[l_pre])
        elif l_pre > r_pre:
            # prevent outing of range
            return None
        val = preorder[l_pre]
        root = TreeNode(val)
        if val in inorder[l_in:r_in+1]:
            i = inorder[l_in:r_in+1].index(val)
        else:
            raise Exception('Invalid Input: Not A Binary Tree')
        root.left = construct_recursion(preorder, l_pre+1, l_pre+i, inorder, l_in, l_in+i-1)
        root.right = construct_recursion(preorder, l_pre+i+1, r_pre, inorder, l_in+i+1, r_in)
        return root

    if preorder:
        root = construct_recursion(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        return root
    else:
        raise Exception('EMPTY INPUT!')


root = construct_binary_tree2([1,2,3],[3,2,1])
print()
