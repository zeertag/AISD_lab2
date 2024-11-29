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
                    return
            if walking_node.key < key:
                walking_node = walking_node.right_child
            else:
                walking_node = walking_node.left_child
            if walking_node is None:
                print("No key found")

    # Обходы
    #симметричный
    def inorderWalk(self, node):
        if node is None:
            return
        self.inorderWalk(node.left_child)
        print(node.data, end=' ')
        self.inorderWalk(node.right_child)

    #прямой
    def preorderWalk(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorderWalk(node.left_child)
        self.preorderWalk(node.right_child)

    #обратный
    def postorderWalk(self, node):
        if node is None:
            return
        self.postorderWalk(node.left_child)
        self.postorderWalk(node.right_child)
        print(node.data, end=' ')

    def wideWalk(self, node, type=0):
        if node is None:
            print("Tree is empty")
            return
        q = Queue()
        q.put(node)
        while not q.empty():
            k = q.qsize()
            for i in range(k):
                elem = q.get()
                if elem is not None:
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

    def print_tree_with_color(self, node=None, level=0, prefix="Root: "):
        """Выводит дерево с отступами и цветом узлов (черный или красный)."""
        if node is None:
            node = self.root  # если не передан узел, начинаем с корня

        if node is not None:
            # Выводим цветной ключ узла
            if node.color == "Black":
                print(" " * (level * 4) + prefix + Back.BLACK + str(node.key) + Style.RESET_ALL)
            else:
                print(" " * (level * 4) + prefix + Back.RED + str(node.key) + Style.RESET_ALL)

            # Рекурсивный вызов для левого и правого детей
            if node.left_child is not None or node.right_child is not None:
                if node.left_child is not None:
                    self.print_tree_with_color(node.left_child, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right_child is not None:
                    self.print_tree_with_color(node.right_child, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
        else:
            print("Tree is empty")