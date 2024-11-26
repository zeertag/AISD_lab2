class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

        self.color = "Red"

        self.balance = 0
        self.height = 1
