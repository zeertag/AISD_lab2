from BST import BST


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
