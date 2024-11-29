from BST import BST
from Node import Node


class RBT(BST):
    def update_params(self):
        if self.last == self.root:
            self.last.color = "Black"  # Корень всегда черный
            return

        node = self.last

        # Когда родитель красный, необходимо корректировать
        while node != self.root and node.parent.color == "Red":
            uncle, grandparent = self.get_relatives(node)

            # Случай 1: родитель — левый ребенок, дядя — красный
            if node.parent == grandparent.left_child:
                if uncle is not None and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    node = grandparent  # Переходим к дедушке
                else:
                    # Случай 2: если текущий узел — левый ребенок
                    if node == node.parent.left_child:
                        node.parent.color = "Black"
                        grandparent.color = "Red"
                        node = node.parent.parent
                        self.right_rotate(grandparent)
                    else:  # Случай 3: если текущий узел — правый ребенок
                        node = node.parent
                        self.left_rotate(node)
                        node.parent.color = "Black"
                        grandparent.color = "Red"
                        self.right_rotate(grandparent)
            else:  # Если родитель — правый ребенок
                if uncle is not None and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    node = grandparent
                else:
                    # Случай 4: если текущий узел — правый ребенок
                    if node == node.parent.right_child:
                        node.parent.color = "Black"
                        grandparent.color = "Red"
                        node = node.parent.parent
                        self.left_rotate(grandparent)
                    else:  # Случай 5: если текущий узел — левый ребенок
                        node = node.parent
                        self.right_rotate(node)
                        node.parent.color = "Black"
                        grandparent.color = "Red"
                        self.left_rotate(grandparent)

        self.root.color = "Black"  # Корень всегда черный

    def rbt_delete(self, key):
        walking_node = self.root
        node_to_delete = None

        # Поиск узла для удаления
        while walking_node is not None:
            if walking_node.key == key:
                node_to_delete = walking_node
                break
            elif walking_node.key < key:
                walking_node = walking_node.right_child
            else:
                walking_node = walking_node.left_child

        if node_to_delete is None:
            print("Key not found")
            return

        # Если у узла есть два потомка, заменяем его на преемника
        if node_to_delete.left_child is not None and node_to_delete.right_child is not None:
            walking_node = node_to_delete.right_child
            while walking_node.left_child is not None:
                walking_node = walking_node.left_child

            node_to_delete.key = walking_node.key
            node_to_delete.data = walking_node.data

            node_to_delete = walking_node

        # Если узел — лист
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_to_delete.color == "Red":
                if node_to_delete.parent:
                    if node_to_delete.parent.left_child == node_to_delete:
                        node_to_delete.parent.left_child = None
                    else:
                        node_to_delete.parent.right_child = None
            else:
                if self.root == node_to_delete:
                    self.root = None
                    return
                self.fix_double_black(node_to_delete)
                if node_to_delete.parent.left_child == node_to_delete:
                    node_to_delete.parent.left_child = None
                else:
                    node_to_delete.parent.right_child = None

        # Если у узла есть только левый потомок
        elif node_to_delete.left_child is not None:
            node_to_delete.left_child.color = "Black"
            node_to_delete.left_child.parent = node_to_delete.parent
            if self.root == node_to_delete:
                self.root = node_to_delete.left_child
            else:
                if node_to_delete.parent.left_child == node_to_delete:
                    node_to_delete.parent.left_child = node_to_delete.left_child
                else:
                    node_to_delete.parent.right_child = node_to_delete.left_child

        # Если у узла есть только правый потомок
        elif node_to_delete.right_child is not None:
            node_to_delete.right_child.color = "Black"
            node_to_delete.right_child.parent = node_to_delete.parent
            if self.root == node_to_delete:
                self.root = node_to_delete.right_child
            else:
                if node_to_delete.parent.left_child == node_to_delete:
                    node_to_delete.parent.left_child = node_to_delete.right_child
                else:
                    node_to_delete.parent.right_child = node_to_delete.right_child

    def fix_double_black(self, node):
        while node != self.root and (node.color == "Black" or node is None):
            if node == node.parent.left_child:
                sibling = node.parent.right_child

                if sibling and sibling.color == "Red":
                    sibling.color = "Black"
                    node.parent.color = "Red"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right_child

                if (sibling is None or sibling.color == "Black") and \
                        (sibling is None or sibling.left_child is None or sibling.left_child.color == "Black") and \
                        (sibling is None or sibling.right_child is None or sibling.right_child.color == "Black"):
                    if sibling:
                        sibling.color = "Red"
                    node = node.parent
                else:
                    if sibling and sibling.right_child and sibling.right_child.color == "Red":
                        sibling.color = node.parent.color
                        node.parent.color = "Black"
                        sibling.right_child.color = "Black"
                        self.left_rotate(node.parent)
                        node = self.root
                    else:
                        if sibling and sibling.left_child and sibling.left_child.color == "Red":
                            sibling.left_child.color = sibling.color
                            sibling.color = node.parent.color
                            self.right_rotate(sibling)
                            sibling = node.parent.right_child

                        sibling.color = node.parent.color
                        node.parent.color = "Black"
                        if sibling.right_child:
                            sibling.right_child.color = "Black"
                        self.left_rotate(node.parent)
                        node = self.root
            else:
                sibling = node.parent.left_child

                if sibling and sibling.color == "Red":
                    sibling.color = "Black"
                    node.parent.color = "Red"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left_child

                if (sibling is None or sibling.color == "Black") and \
                        (sibling.left_child is None or sibling.left_child.color == "Black") and \
                        (sibling.right_child is None or sibling.right_child.color == "Black"):
                    if sibling:
                        sibling.color = "Red"
                    node = node.parent
                else:
                    if sibling and sibling.left_child and sibling.left_child.color == "Red":
                        sibling.color = node.parent.color
                        node.parent.color = "Black"
                        sibling.left_child.color = "Black"
                        self.right_rotate(node.parent)
                        node = self.root
                    else:
                        if sibling and sibling.right_child and sibling.right_child.color == "Red":
                            sibling.right_child.color = sibling.color
                            sibling.color = node.parent.color
                            self.left_rotate(sibling)
                            sibling = node.parent.left_child

                        sibling.color = node.parent.color
                        node.parent.color = "Black"
                        if sibling.left_child:
                            sibling.left_child.color = "Black"
                        self.right_rotate(node.parent)
                        node = self.root

        if node:
            node.color = "Black"

    def get_relatives(self, node):
        if node.parent.parent is None:
            uncle = None
            grand_p = None
        else:
            grand_p = node.parent.parent
            if node.parent == grand_p.left_child:
                uncle = grand_p.right_child
            else:
                uncle = grand_p.left_child
        return uncle, grand_p

    def right_rotate(self, node):
        a = node
        b = node.left_child
        b.parent = a.parent
        a.left_child = b.right_child
        if b.right_child is not None:
            b.right_child.parent = a
        if a.parent is not None:
            if a.parent.left_child == a:
                a.parent.left_child = b
            else:
                a.parent.right_child = b
        b.right_child = a
        a.parent = b
        if self.root == a:
            self.root = b

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

        return b

    def is_rbt_valid(self):
        if self.root is None:
            return True  # Пустое дерево всегда корректно

        # Проверка правила 2: Корень должен быть черным
        if self.root.color != "Black":
            print("Root is not black")
            return False

        # Проверка правил 1, 3 и 4 (цвет узлов и черная высота)
        return self._check_black_height(self.root) != -1

    def _check_black_height(self, node):
        if node is None:
            return 1  # Лист является черным

        # Проверка правила 1: Каждый узел либо красный, либо черный
        if node.color not in ("Red", "Black"):
            print(f"Node {node.key} has invalid color: {node.color}")
            return -1

        # Проверка правила 4: Нет двух последовательных красных узлов
        if node.color == "Red":
            if (node.left_child and node.left_child.color == "Red") or (
                    node.right_child and node.right_child.color == "Red"):
                print(f"Red violation at node {node.key}")
                return -1

        # Рекурсивная проверка для детей
        left_black_height = self._check_black_height(node.left_child)
        right_black_height = self._check_black_height(node.right_child)

        # Если одно из поддеревьев не корректно, возвращаем -1
        if left_black_height == -1 or right_black_height == -1:
            return -1

        # Проверка правила 5: Черная высота должна быть одинаковой для всех путей
        if left_black_height != right_black_height:
            print(f"Black height violation at node {node.key}")
            return -1

        # Если узел черный, увеличиваем черную высоту
        return left_black_height + (1 if node.color == "Black" else 0)