from Node import Node
from queue import Queue
from colorama import Back, Style


class BST:
    def __init__(self):
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

    # Обходы
    def inorderWalk(self, node: Node):
        if node == None:
            return
        self.inorderWalk(node.left_child)
        print(node.key, end=' ')
        self.inorderWalk(node.right_child)

    def wideWalk(self, node: Node, type=0):
        q = Queue()
        q.put(node)
        while not q.empty():
            k = q.qsize()
            for i in range(k):
                elem = q.get()
                if type == 0:
                    print(elem.key, end=' ')
                elif type == 1:
                    print(f'{elem.key} (Height: {elem.height}, Balance: {elem.balance})', end=' ')
                else:
                    if elem.color == "Black":
                        print(Back.BLACK + str(elem.key) + Style.RESET_ALL, end=' ')
                    else:
                        print(Back.RED + str(elem.key) + Style.RESET_ALL, end=' ')
                if elem.left_child is not None:
                    q.put(elem.left_child)
                if elem.right_child is not None:
                    q.put(elem.right_child)
            print()
