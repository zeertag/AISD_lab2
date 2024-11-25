import random


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

        self.color = None

        self.balance = 0
        self.height = 1


class BST:
    def __init__(self):
        self.length = 0
        self.root = None
        self.last = None

    def find(self, key):
        walking_node = self.root
        while walking_node is not None:
            if walking_node.key == key:
                return walking_node.data
            if walking_node.key < key:
                walking_node = walking_node.right_child
            else:
                walking_node = walking_node.left_child
        return "No data found"

    def insert(self, key, data):
        new_node = Node(key, data)
        walking_node = self.root
        if walking_node is None:
            self.root = new_node
            self.last = self.root
            return

        while walking_node is not None:
            if walking_node.key == key:
                self.last = None
                return "Key is already exist"
            elif key > walking_node.key:
                if walking_node.right_child is not None:
                    walking_node = walking_node.right_child
                else:
                    walking_node.right_child = new_node
                    new_node.parent = walking_node
                    self.last = new_node
                    return
            else:
                if walking_node.left_child is not None:
                    walking_node = walking_node.left_child
                else:
                    walking_node.left_child = new_node
                    new_node.parent = walking_node
                    self.last = new_node
                    return

    def delete(self, key):
        if self.root is None:
            return "Zero Tree"
        walking_node = self.root
        while walking_node is not None:
            if walking_node.key == key:
                if walking_node.left_child is None and walking_node.right_child is None:
                    if walking_node.key == self.root.key:
                        self.root = None
                    else:
                        if walking_node.parent.left_child == walking_node:
                            walking_node.parent.left_child = None
                        else:
                            walking_node.parent.right_child = None
                    self.last = walking_node.parent
                    return

                elif walking_node.left_child is not None and walking_node.right_child is None:
                    if walking_node.key == self.root.key:
                        self.root = walking_node.left_child
                        self.root.parent = None
                    else:
                        if walking_node.parent.left_child == walking_node:
                            walking_node.parent.left_child = walking_node.left_child
                        else:
                            walking_node.parent.right_child = walking_node.left_child
                        walking_node.left_child.parent = walking_node.parent
                    self.last = walking_node.parent
                    return

                elif walking_node.left_child is None and walking_node.right_child is not None:
                    if walking_node.key == self.root.key:
                        self.root = walking_node.right_child
                        self.root.parent = None
                    else:
                        if walking_node.parent.left_child == walking_node:
                            walking_node.parent.left_child = walking_node.right_child
                        else:
                            walking_node.parent.right_child = walking_node.right_child
                        walking_node.right_child.parent = walking_node.parent
                    self.last = walking_node.parent
                    return

                else:
                    temp_node = walking_node.right_child
                    self.last = temp_node
                    while temp_node.left_child is not None:
                        temp_node = temp_node.left_child
                        self.last = temp_node.parent

                    if walking_node.key == self.root.key:
                        self.root = temp_node
                    elif walking_node.parent.left_child == walking_node:
                        walking_node.parent.left_child = temp_node
                    else:
                        walking_node.parent.right_child = temp_node

                    if temp_node.parent != walking_node:
                        temp_node.parent.left_child = temp_node.right_child
                        if temp_node.right_child is not None:
                            temp_node.right_child.parent = temp_node.parent
                        temp_node.right_child = walking_node.right_child
                        walking_node.right_child.parent = temp_node
                    temp_node.left_child = walking_node.left_child
                    walking_node.left_child.parent = temp_node
                    temp_node.parent = walking_node.parent

                    # old_parent = temp_node.parent
                    # old_child = temp_node.right_child
                    # temp_node.parent = walking_node.parent
                    # temp_node.left_child = walking_node.left_child
                    # if temp_node == walking_node.right_child:
                    #     temp_node.right_child = walking_node.right_child.right_child
                    # else:
                    #     temp_node.right_child = walking_node.right_child
                    #
                    # temp_node.left_child.parent = temp_node
                    # if temp_node.right_child is not None:
                    #     temp_node.right_child.parent = temp_node

                    # old_parent.left_child = old_child
                    # self.root.parent = None

                    # self.last = temp_node.parent
                    return
            if walking_node.key < key:
                walking_node = walking_node.right_child
            else:
                walking_node = walking_node.left_child


class AVL_T(BST):
    def update_params(self):
        walking_node = self.last
        while walking_node is not None:
            walking_node.height = max(self.get_height(walking_node.left_child),
                                      self.get_height(walking_node.right_child)) + 1
            walking_node.balance = self.get_height(walking_node.left_child) - self.get_height(
                walking_node.right_child)

            if abs(walking_node.balance) > 1:
                self.balancing(walking_node)
            # self.length = walking_node.height
            walking_node = walking_node.parent

    def get_height(self, node):
        return node.height if node is not None else 0

    def balancing(self, node):
        # walking_node = self.last
        walking_node = node
        while walking_node is not None:
            if walking_node.balance > 1:
                if walking_node.left_child.balance >= 0:
                    walking_node = self.right_rotate(walking_node)
                else:
                    walking_node.left_child = self.left_rotate(walking_node.left_child)
                    walking_node = self.right_rotate(walking_node)
            elif walking_node.balance < -1:
                if walking_node.right_child.balance <= 0:
                    walking_node = self.left_rotate(walking_node)
                else:
                    walking_node.right_child = self.right_rotate(walking_node.right_child)
                    walking_node = self.left_rotate(walking_node)
            walking_node = walking_node.parent

    def right_rotate(self, node):
        a = node
        b = node.left_child
        b.parent = a.parent
        a.left_child = b.right_child
        if b.right_child is not None:
            b.right_child.parent = a
        # if a.parent is None:
        #     self.last = b
        if a.parent is not None:
            if a.parent.left_child == a:
                a.parent.left_child = b
            else:
                a.parent.right_child = b
        b.right_child = a
        a.parent = b
        if self.root == a:
            self.root = b

        self.update_node_params(a)
        self.update_node_params(b)

        return b

    def left_rotate(self, node):
        a = node
        b = node.right_child
        b.parent = a.parent
        a.right_child = b.left_child
        if b.left_child is not None:
            b.left_child.parent = a
        if a.parent is not None:
            if a.parent.left_child == a:
                a.parent.left_child = b
            else:
                a.parent.right_child = b
        b.left_child = a
        a.parent = b
        if self.root == a:
            self.root = b

        self.update_node_params(a)
        self.update_node_params(b)

        return b

    def update_node_params(self, node):
        if node is None:
            return
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        node.balance = self.get_height(node.left_child) - self.get_height(node.right_child)


class RBT(BST):
    pass

# test_tree = BST()
test_tree = AVL_T()
nums = [random.randint(0, 100) for i in range(10)]
print(nums)
# nums = [84, 793, 89, 874, 61, 937, 113, 928, 797, 665, 481, 374, 45, 822, 842, 616, 50, 488, 649, 734]
for i in nums:
    test_tree.insert(i, str(i))
    test_tree.update_params()
    # test_tree.balancing()
    # print()
    # test_tree.print_tree()

# test_tree.print_tree()
for i in nums:
    print(i, test_tree.find(i))
print("--------------")

# for i in nums:
#     print('--', i)
#     test_tree.delete(i)
#     test_tree.update_params()
    # print()
    # test_tree.print_tree()
    # print()
    # print()
    # print()
    # test_tree.balancing()
# # test_tree.delete(96)
# # test_tree.delete(27)
# # test_tree.delete(31)
# # test_tree.delete(86)
# # test_tree.delete(51)
# # test_tree.delete(84)
# # test_tree.delete(45)
# # test_tree.delete(94)
# # test_tree.delete(2)
# # test_tree.delete(54)
#
# for i in nums:
#     print(i, test_tree.find(i))
