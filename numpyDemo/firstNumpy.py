import numpy as np
# 打印numpy版本
from sklearn.datasets import make_blobs

print(np.__version__)

# 生成数组
my_array = np.array([1, 2, 3, 4, 5])

print(my_array)
# 打印数组形状
print(my_array.shape)
# 根据索引打印数组中的元素
print(my_array[0])
print(my_array[1])
print(my_array[4])
print(my_array[-1])

# 对数组进行分片操作
my_array = np.array([[1, 2], [3, 4]])
print(my_array)
print(my_array.shape)
# 打印指定索引的值
print(my_array[0][0])
# 打印第二列的数据
print("打印第二列数据：", my_array[:, 1])
# 打印第二行的数据
print("打印第二行数据：", my_array[1, :])

print(np.random.uniform(0, 2))


# 生成数据集
x, y = make_blobs(n_samples=400, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                  cluster_std=[0.4, 0.2, 0.2, 0.2])
# 生成数据散点图
# plt.scatter(x[:, 0], x[:, 1], marker='o')
# plt.show()
print([x,y])




