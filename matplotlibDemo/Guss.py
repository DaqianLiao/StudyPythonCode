# coding=utf-8
import math

import matplotlib.pyplot as plt

# 正太分布核函数
def cal_Gaussian(x, h=1):
    molecule = x * x
    denominator = 2 * h * h
    left = 1 / (math.sqrt(2 * math.pi) * h)
    return left * math.exp(-molecule / denominator)


x = []
# 初始化X轴数据
for i in range(-40, 40):
    x.append(i * 0.5)
print("init X = ", x)

score_1 = []
score_2 = []
score_3 = []
score_4 = []

for i in x:
    score_1.append(cal_Gaussian(i, 1))
    score_2.append(cal_Gaussian(i, 2))
    score_3.append(cal_Gaussian(i, 3))
    score_4.append(cal_Gaussian(i, 4))

plt.plot(x, score_1, 'b--', label="h=1")
plt.plot(x, score_2, 'k--', label="h=2")
plt.plot(x, score_3, 'g--', label="h=3")
plt.plot(x, score_4, 'r--', label="h=4")

plt.legend(loc="upper right")
plt.xlabel("x")
plt.ylabel("N")
plt.show()
