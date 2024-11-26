import random
from BST import BST
from AVL import AVL_T
from Red_Black import RBT

# test_tree = BST()
# for i in range(1000, 1000000, 10000):
#     test_tree = AVL_T()
#     nums = [random.randint(0, 1000000000) for _ in range(i)]
#     for j in nums:
#         test_tree.insert(j, str(j))
#         test_tree.update_params()
#     print(test_tree.root.height)


test_tree = RBT()
nums = [random.randint(0, 100) for _ in range(10)]
# nums = [100, 50, 150, 25, 75, 125, 175]
print(nums)
for j in nums:
    msg = test_tree.insert(j, str(j))
    if msg != "Key is already exist":
        test_tree.update_params()

# test_tree.inorderWalk(test_tree.root)
test_tree.wideWalk(test_tree.root, 2)
