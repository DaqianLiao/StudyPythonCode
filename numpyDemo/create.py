# 生成一维数组
import numpy as np

import numpy.random as rd

ones = np.ones(5)
print(ones)
# 生成二维数组
ones_vec = np.ones((2, 3))
print(ones_vec)

zeros = np.zeros(5)
print(zeros)
zeros_vec = np.zeros((2, 5))
print(zeros_vec)

# 生成随机数
random = rd.random()
print(random)

rand = rd.rand(4)
print(rand)

rand = rd.rand(4, 5)
print(rand)

range = np.arange(5)
print("range = ", range)

rangeBystep = np.arange(0, 10, 1)
print("range = ", rangeBystep)

# 从0  到  pi 之间生成20个数
ls = np.linspace(0, np.pi, 20)
print(ls)

rand = rd.rand(4)
print(rand)
print(rand.sum())
print(rand.max())
print(rand.min())

rand = rd.rand(4, 5)
print(rand)
print(rand.sum())
print(rand.max())
print(rand.min())

a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(a)
print(b)
print(c)

# 创建全是true 类型的布尔数组
bool_ture = np.full((2, 2), True, dtype=bool)
print(bool_ture)
bool_ture = np.ones((2, 2), dtype=bool)
print(bool_ture)

# 将数据转化为指定的行列
source = np.arange(8)
newshape = source.reshape(2, -1)
print(newshape)
newshape = source.reshape(4, 2)
print(newshape)

# 随机产生1-5之间的整数，生成2行3列的矩阵
a = np.random.randint(1, 5, size=(2, 3))
print(a)

# 随机产生1-5之间的浮点数，生成2行3列的矩阵
a = np.random.random((2, 3)) + np.random.randint(1, 5, size=(2, 3))
print(a)


# 保留小数点后3位
np.set_printoptions(3)
print(a)




