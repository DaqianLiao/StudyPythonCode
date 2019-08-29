import numpy as np

a = np.array([[0, 2], [1, 3]])
b = np.array([[1, 2], [3, 4]])
# 对应位置的四则运算
sum = a + b
diff = a - b
product = a * b
quotient = a / b
print("sum = ", sum)
print("diff = ", diff)
print("product = ", product)
print("sumquotient = ", quotient)

# 矩阵运算 点乘
matrix_product = a.dot(b)
print(a, b)
print("matrix product = ", matrix_product)

# 前后连接两个数组
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# 垂直连接两个数组
ans1 = np.concatenate([a, b], axis=0)
ans2 = np.vstack([a, b])
print(ans1)
print(ans2)

# 首尾连接两个数组
ans3 = np.concatenate([a, b], axis=1)
print(ans3)
ans4 = np.hstack([a, b])
print(ans4)

# 将数组中的每个元素重复3次，循环4次
a = np.array([1, 2, 3])
print(np.repeat(a, 3))
print(np.tile(a, 4))

a = np.array([1, 2, 3, 5])
b = np.array([1, 2, 3, 4])
# 求两个集合中的交集
print(np.intersect1d(a, b))
# 求交集的索引位置
print(np.where(a == b)[0])
# 求两个集合的差集
print(np.setdiff1d(a, b))

a = np.arange(15)
# 过滤器
print(a[np.where((a < 10) & (a > 6))[0]])
print(a[(a >= 5) & (a <= 10)])

# 交换数组中的列顺序
a = np.arange(9)
print(a)
b = a.reshape([3, 3])
print(b)
print(b[:, [0, 2, 1]])
# 反转列顺序
print(b[::-1])
# 交换行顺序
print(b[[1, 2, 0], :])
# 反转行顺序
print(b[:, ::-1])

a = 2
print("原始数据：", a)
print("原始平方数据：", a ** 2)
print("原始立方数据：", a ** 3)
