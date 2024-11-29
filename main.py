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


# test_tree = RBT()
# nums = [random.randint(0, 1000000) for _ in range(1000)]
# # nums = [787, 816, 582, 131, 114, 836, 513, 999, 484, 212]
# # nums = [786552, 721750, 52888, 6616, 477849, 883654, 301121, 138695, 732239, 301047]
# print(nums)
# for j in nums:
#     msg = test_tree.insert(j, str(j))
#     if msg != "Key is already exist":
#         test_tree.update_params()
# test_tree.print_tree_with_color()
# print()
# print()
# for j in nums:
#     test_tree.rbt_delete(j)
#     test_tree.print_tree_with_color()
#     if test_tree.is_rbt_valid():
#         print("ГООООООООЛ")
#     else:
#         print("не гол :(")
#         break
#     print()
#     print()


test_tree = BST()
test_tree.insert(100, "A")
test_tree.insert(150, "C")
test_tree.insert(200, "F")
test_tree.insert(50, "B")
test_tree.insert(25, "D")
test_tree.insert(75, "E")

test_tree.preorderWalk(test_tree.root)
print()
test_tree.inorderWalk(test_tree.root)
print()
test_tree.postorderWalk(test_tree.root)
