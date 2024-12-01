import random
from BST import BST
from AVL import AVL_T
from Red_Black import RBT
from Sort import MergeSort
from graphs import make_graphs

# bst_h = []
# for i in range(1000, 100000, 1000):
#     arr = random.sample(range(1, 1000000), i)
#     tree = BST()
#     for j in arr:
#         tree.insert(j, str(j))
#     tree.get_height()
#     bst_h.append(tree.height)
#
bst_h = [20, 28, 28, 25, 28, 34, 31, 31, 30, 30, 34, 32, 29, 31, 31, 33, 31, 33, 33, 34, 31, 34, 33, 37, 41, 34, 36, 35,
         40, 34, 35, 38, 36, 33, 36, 38, 39, 38, 37, 40, 38, 35, 39, 37, 41, 38, 42, 37, 33, 39, 40, 39, 35, 38, 42, 40,
         34, 37, 42, 41, 39, 37, 37, 43, 38, 37, 44, 37, 40, 42, 40, 38, 39, 40, 36, 42, 39, 39, 45, 39, 38, 37, 41, 42,
         41, 38, 40, 39, 45, 42, 39, 36, 41, 39, 43, 42, 38, 46, 41]
make_graphs([i for i in range(1000, 100000, 1000)], bst_h, "Бинарное дерево поиска", "bst_log.png")
#
# rbt_h = []
#
# for i in range(1000, 100000, 1000):
#     test_tree = RBT()
#     nums = MergeSort([random.randint(0, 100000000) for _ in range(i)])
#     for j in nums:
#         msg = test_tree.insert(j, str(j))
#         if msg != "Key is already exist":
#             test_tree.update_params()
#     test_tree.get_height()
#     rbt_h.append(test_tree.height)
rbt_h = [17, 19, 20, 21, 22, 22, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27,
         27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29,
         29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
         30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31]
make_graphs([i for i in range(1000, 100000, 1000)], rbt_h, "Красно-черное дерево", "rbt_log.png")
#
# avl_h = []
#
# for i in range(1000, 100000, 1000):
#     test_tree = AVL_T()
#     nums = MergeSort([random.randint(0, 100000000) for _ in range(i)])
#     for j in nums:
#         msg = test_tree.insert(j, str(j))
#         if msg != "Key is already exist":
#             test_tree.update_params()
#     test_tree.get_height()
#     avl_h.append(test_tree.height)
avl_h = [10, 11, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
         15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
         16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
         17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]
make_graphs([i for i in range(1000, 100000, 1000)], avl_h, "АВЛ-дерево", "avl_log.png")
#
# print("Значения высот для 1000 -> 100000 шаг 1000")
# print("BST")
# print(bst_h)
# print()
# print("RBT")
# print(rbt_h)
# print()
# print("AVL")
# print(avl_h)
#
# with open("Graphs/heights.txt", "w", encoding="utf-8") as file:
#     file.write("Значения высот для 1000 -> 100000 шаг 1000\n")
#     file.write("BST (ключи распределены равномерно)\n")
#     file.write(f"{bst_h}\n\n")
#     file.write("RBT (ключи монотонно возрастают)\n")
#     file.write(f"{rbt_h}\n\n")
#     file.write("AVL (ключи монотонно возрастают)\n")
#     file.write(f"{avl_h}\n\n")