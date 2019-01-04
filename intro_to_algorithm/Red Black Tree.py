class Red_Black_Tree(object):

    class __Node(object):

        def __init__(self, key, value=None, color=None, parent=None, left=None, right=None):
            self.key = key
            self.value = value
            self.color = color  # black = 0 red = 1
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.__NIL = self.__Node('NIL')
        self.__NIL.color = 0
        self.__NIL.value = None
        self.__NIL.left = self.__NIL.right = self.__NIL
        self.__root = self.__Node(None)
        self.__root.color = 0
        self.__root.left = self.__NIL
        self.__root.right = self.__NIL
        self.__root.parent = self.__NIL

    def __find_node(self, key):
        # return key's uplvl
        node = self.__root
        while True:
            if key < node.key:
                flow = 'left'
            else:
                flow = 'right'
            next_node = getattr(node, flow)
            if next_node is self.__NIL or next_node.key == key:
                return (node, flow)
            else:
                node = next_node

    def get(self, key):
        node, flow = self.__find_node(key)
        node = getattr(node, flow)
        if node is self.__NIL:
            val  = 'Non-Existent'
        else:
            val = node.value
        return val

    # def __node_switch(self, node, node_link, target, target_link):
    #     '''
    #     link [node]'s [nlink] to [target]'s [target link]
    #     :param node: change node
    #     :param node_link: left or right or parent
    #     :param target: link to where
    #     :param target_link: left or right or parent
    #     :return: None
    #     '''
    #     # change parent
    #     if node_link == 'parent':
    #         current_p = node.parent
    #         # parent unlink
    #         if current_p.left == node:
    #             current_p.left = None
    #         else:
    #             current_p.right =None
    #         # link to new parent
    #         setattr(target, target_link, node)
    #         setattr(node, node_link, target)
    #     # change left child
    #     if node_link in ['left','right']:
    #         # clean old child's parent
    #         getattr(node, node_link).parent = None
    #         # link new child
    #         setattr(node, node_link, target)
    #         setattr(target, target_link, node)

    def __left_rotate(self, node):
        y = node.right
        y.parent = node.parent
        if node.parent == self.__NIL:
            self.__root = y
        else:
            if node.parent.left == node:
                node.parent.left = y
            else:
                node.parent.right = y
        node.parent = y
        node.right = y.left
        y.left = node
        return

    def __right_rotate(self, node):
        x = node.left
        x.parent = node.parent
        if node.parent == self.__NIL:
            self.__root = x
        else:
            if node.parent.left == node:
                node.parent.left = x
            else:
                node.parent.right = x
        node.parent = x
        node.left = x.right
        x.right = node
        return

    def __recolor(self, node):
        '''
        # case 1
        # node and parent is red 1 -> 0
        # node's uncle is red 1 -> 0
        # parent parent is black 0 -> 1
        :param node: conflict node
        :return: node's grandparent
        '''
        node.parent.parent.color = 1
        node.parent.parent.left.color = 0
        node.parent.parent.right.color = 0
        return node.parent.parent

    def __insert_fix_up(self, insert_node):

        conflict = insert_node
        while conflict.parent.color == 1:
            if conflict.parent.parent.left == conflict.parent:
                # insert_node is a right node
                # position = 'right'
                y = conflict.parent.parent.right
                if y.color == 1:
                    # case 1
                    conflict = self.__recolor(conflict)
                else:
                    if conflict.parent.right == conflict:
                        # case 2
                        conflict = conflict.parent
                        self.__left_rotate(conflict)
                    # case 3
                    conflict.parent.color = 0
                    conflict.parent.parent.color = 1
                    self.__right_rotate(conflict.parent.parent)
            else:
                # insert_node is a left node
                # position = 'left'
                y = conflict.parent.parent.left
                if y.color == 1:
                    # case 1
                    conflict = self.__recolor(conflict)
                else:
                    if conflict.parent.left == conflict:
                        # case 2
                        self.__right_rotate(conflict.parent)
                    # case 3
                    conflict.parent.color = 0
                    conflict.parent.parent.color = 1
                    self.__left_rotate(conflict.parent.parent)
            # y = getattr(conflict.parent.parent, position)
            # case_2 = {'right':'__left_rotate', 'left':'__right_rotate'}
            # case_3 = {'left': '__left_rotate', 'right': '__right_rotate'}
            # if y.color == 1:
            #     # case 1
            #     conflict = self.__recolor(conflict)
            # else:
            #     if getattr(conflict.parent, position) == conflict:
            #         # case 2
            #         getattr(self,case_2[position])(conflict.parent)
            #     # case 3
            #     conflict.parent.color = 0
            #     conflict.parent.parent.color = 1
            #     getattr(self, case_3[position])(conflict.parent.parent)
        self.__root.color = 0 # root is black

        return

    def insert(self, key, value = None):
        # key，value可以为可迭代对象
        if self.__root.key is None:
            new_node = self.__root
        else:
            new_node = self.__Node(key)
            parent, flow = self.__find_node(key)
            setattr(parent, flow, new_node)
            new_node.parent = parent
        new_node.key = key
        new_node.value = value
        new_node.color = 1 # RED
        new_node.left = self.__NIL
        new_node.right = self.__NIL
        self.__insert_fix_up(new_node)
        return


    def dins(self, key_value):
        # key_value 是一个 键为key 值为value的字典
        for key in key_value:
            self.insert(key, key_value[key])
        return

    def max(self, node):
        while node.right is not self.__NIL:
            node = node.right
        return node

    def min(self, node):
        while node.left is not self.__NIL:
            node = node.left
        return node

    def __delete_fix_up(self, node):
        # node = delnode.child when del delnode delnode's subtree height -1
        # if node is red then color node to black --> subtree height +1 --> OK
        # if node is black 3 condition
        # condition 1: node.p = black node.p.other child = black
        # condition 2：node.p = black node.p.other child = red
        # condition 3: node.p = red node.p.other child = black (actually same as condition 1)
        # case 1 sol(condition 2 sol): node.p -> red; node.p.another child -> black; LR(node.p); turn to case 2\3\4
        # condition 1\3: case 2: node.p.other child.child both black
        #                case 3: node.p.other child.left red, right black
        #                case 4: node.p.other child.right red, left whatever
        # case 2 sol: node.p.another child --> red then node.p subtree height both -1 so node.p should--> black
        #            if node.p = red then node.p -> black, height +1; FINISH else _delete_fix_up(node.p(double black))
        # case 3 sol: node.p.other child -> red; node.p.other child.left -> black; RR(node.p.other child) turn to case 4
        # case 4 sol: node.p --> black; node.p.other child --> red; node.p.other child.right --> black;LR(node.p); FINISH
        while node is not self.__root and node.color == 0:
            if node is node.parent.left:
                other_child = node.parent.right
                if node.parent.color == 0 and other_child.color == 1:
                    # case 1
                    node.parent.color = 1
                    other_child.color = 0
                    self.__left_rotate(node.parent)
                    other_child = node.parent.right
                if other_child.left.color == 0 and other_child.right.color == 0:
                    # case 2
                    other_child.color = 1
                    node = node.parent
                else:
                    if other_child.left.color == 1 and other_child.right.color == 0:
                        # case 3
                        other_child.color = 1
                        other_child.left.color = 0
                        self.__right_rotate(other_child)
                    # case 4
                    node.parent.color = 0
                    other_child.color = 1
                    other_child.right.color = 0
                    self.__left_rotate(node.parent)
                    node = self.__root
            else:
                other_child = node.parent.left
                if node.parent.color == 0 and other_child.color == 1:
                    # case 1
                    node.parent.color = 1
                    other_child.color = 0
                    self.__right_rotate(node.parent)
                    other_child = node.parent.right
                if other_child.left.color == 0 and other_child.right.color == 0:
                    # case 2
                    other_child.color = 1
                    node = node.parent
                else:
                    if other_child.right.color == 1 and other_child.left.color == 0:
                        # case 3
                        other_child.color = 1
                        other_child.right.color = 0
                        self.__left_rotate(other_child)
                    # case 4
                    node.parent.color = 0
                    other_child.color = 1
                    other_child.left.color = 0
                    self.__right_rotate(node.parent)
                    node = self.__root
        node.color = 0 # for condition 2 and case 2-1
        return

    def delete(self, key):
        # 叶子节点
        node = self.__getnode(key)
        # 如果是叶子节点 删除node 如果是只有左或者只有右 删除node 将子节点接上node的父节点 如果有左有由 将后继的key放入node 删除后继
        delnode = node if node.left is self.__NIL or node.right is self.__NIL else self.min(node.right) # 后继：右子树中的最小值
        delnode_child = delnode.left if delnode.left is not self.__NIL else delnode.right # 子树，如果是叶子 左=右=nil
        delnode_child.parent = delnode.parent # 将子树的父改为删除节点的父
        if delnode.parent is self.__NIL:
            # 判断是否是根节点
            self.__root = delnode_child
        else:
            if delnode == delnode.parent.left:
                #删除的节点是其父的左
                delnode.parent.left = delnode_child
            else:
                # 删除的节点是其父的右
                delnode.parent.right = delnode_child
        if delnode is not node:
            # 如果删除的是后继 将后继的key覆盖node的key
            node.key = delnode.key
        if delnode.color == 0:
            #如果删除的是一个黑节点将违反黑节点高度原则 进行修复
            self.__delete_fix_up(delnode_child)
        return
    # 中序遍历
    # 二叉树可视化打印
    def visual(self):

        return

RBT = Red_Black_Tree()
# RBT.insert(11)
# RBT.insert(2)
# RBT.insert(14)
# RBT.insert(1)
# RBT.insert(7)
# RBT.insert(15)
# RBT.insert(5)
# RBT.insert(8)
# RBT.insert(4)
a = dict(zip([11,2,14,1,7,15,5,8,4],[11,2,14,1,7,15,5,8,4]))
RBT.dins(a)
print(RBT.get(1))
print(RBT.get(3))
print()


