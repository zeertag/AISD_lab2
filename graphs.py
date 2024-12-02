import numpy as np
import matplotlib.pyplot as plt
import os


def make_graphs(sizes, arr_h, name, filename="graph.png", save_path="Graphs"):
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, arr_h, 'o-', label=name, markersize=8)
    log_values = np.log2(sizes) #1.8RBT  2.5BST
    plt.plot(sizes, log_values, 'r--', label=r'Функция $\log2(n)$', linewidth=2)
    plt.title('Зависимость высоты дерева от количества ключей', fontsize=14)
    plt.xlabel('Количество элементов', fontsize=12)
    plt.ylabel('Высота дерева', fontsize=12)
    plt.grid()
    plt.legend(fontsize=10, loc='upper left')
    plt.tight_layout(pad=2.0)

    save_file_path = os.path.join(save_path, filename)
    plt.savefig(save_file_path)

    # plt.show()