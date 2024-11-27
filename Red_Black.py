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

    def balancing(self):
        # ... (rest of the function remains unchanged)

        while node != self.root and node.color == "Black":
            sibling = self.get_sibling(node)

            # Handle the case when node is the root
            if node.parent is None:
                break

            # Case 1: Sibling is red
            if sibling and sibling.color == "Red":
                sibling.color = "Black"  # Change sibling to black
                node.parent.color = "Red"  # Change parent to red
                self.rotate(node, sibling)  # Perform rotation based on node position
                node = sibling  # Update node for next iteration

            # Case 2: Sibling is black and both children are black
            elif (sibling is None or sibling.left_child is None or sibling.left_child.color == "Black") and \
                    (sibling is None or sibling.right_child is None or sibling.right_child.color == "Black"):
                if sibling:
                    sibling.color = "Red"  # Change sibling to red (prepare for borrow)
                node = node.parent  # Move up the tree

            # Case 3: Sibling is black and has a red right child
            elif sibling and (sibling.right_child is None or sibling.right_child.color == "Black"):
                if sibling.left_child:
                    sibling.left_child.color = "Black"  # Change left child to black
                sibling.color = "Red"  # Change sibling to red
                self.rotate(node, sibling, "left")  # Left rotation based on node position
                sibling = self.get_sibling(node)  # Update sibling for next iteration

            # Case 4: Sibling is black and has a red left child
            else:
                sibling.color = node.parent.color  # Change sibling color to parent's color
                node.parent.color = "Black"  # Change parent to black
                if sibling.right_child:
                    sibling.right_child.color = "Black"  # Change right child to black
                self.rotate(node, sibling, "right")  # Right rotation based on node position
                node = self.root  # Update node to root for next iteration (balancing complete)

            # After balancing, ensure root is black
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

    def get_sibling(self, node):
        if node.parent is None:
            return None
        if node == node.parent.left_child:
            return node.parent.right_child
        else:
            return node.parent.left_child

    def rotate(self, node, sibling, direction="right"):
        if direction == "right":
            self.right_rotate(node)
        else:
            self.left_rotate(node)
