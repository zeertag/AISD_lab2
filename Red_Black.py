from BST import BST


class RBT(BST):
    def update_params(self):
        if self.last == self.root:
            self.last.color = "Black"
        else:
            walking_node = self.last
            if self.last.parent.color == "Black":
                return

            while walking_node != self.root and walking_node.parent.color == "Red":
                uncle, grand_p = self.get_relatives(walking_node)
                if walking_node.parent == grand_p.left_child:
                    if uncle is not None and uncle.color == "Red":
                        walking_node.parent.color = "Black"
                        uncle.color = "Black"
                        grand_p.color = "Red"
                        walking_node = grand_p
                    else:
                        if walking_node == walking_node.parent.left_child:
                            walking_node.parent.color = "Black"
                            grand_p.color = "Red"
                            walking_node = walking_node.parent.parent
                            walking_node = self.right_rotate(walking_node)
                        else:
                            walking_node.color = "Black"
                            grand_p.color = "Red"
                            walking_node = walking_node.parent
                            walking_node = self.left_rotate(walking_node)
                            walking_node = walking_node.parent
                            walking_node = self.right_rotate(walking_node)
                else:
                    if uncle is not None and uncle.color == "Red":
                        walking_node.parent.color = "Black"
                        uncle.color = "Black"
                        grand_p.color = "Red"
                        walking_node = grand_p
                    else:
                        if walking_node == walking_node.parent.right_child:
                            walking_node.parent.color = "Black"
                            grand_p.color = "Red"
                            walking_node = walking_node.parent.parent
                            walking_node = self.left_rotate(walking_node)
                        else:
                            walking_node.color = "Black"
                            grand_p.color = "Red"
                            walking_node = walking_node.parent
                            walking_node = self.right_rotate(walking_node)
                            walking_node = walking_node.parent
                            walking_node = self.left_rotate(walking_node)
            self.root.color = "Black"

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
