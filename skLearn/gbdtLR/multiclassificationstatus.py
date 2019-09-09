import numpy as np

import sklearn.metrics as mt

y_pred = [0, 2, 1, 3, 9, 9, 5, 8]
y_true = [0, 1, 2, 3, 2, 6, 5, 9]

# 1 准确率
print(mt.accuracy_score(y_true, y_pred))

# average in ['micro','None','macro','samples','weighted']
# 微平均，精确率
print(mt.precision_score(y_pred, y_true, average='micro'))

# 宏平均，精确率
print(mt.precision_score(y_pred, y_true, average='macro'))

print(mt.precision_score(y_true, y_pred, labels=[0, 1, 2, 3], average='macro'))

# 2 召回率
print(mt.recall_score(y_pred, y_true, average='micro'))
print(mt.recall_score(y_pred, y_true, average='macro'))

# 3 F1
print(mt.f1_score(y_true, y_pred, average='weighted'))

# 混淆矩阵
print(mt.confusion_matrix(y_true, y_pred))
print(mt.confusion_matrix(y_true, y_pred, labels=[0, 1, 2]))

# 分类报告
print(mt.classification_report(y_true, y_pred, labels=[0, 0]))

# 距离
y_dis_pred = [1, 2, 3, 4]
y_dis_true = [2, 2, 3, 4]
print(" 海明距离：", mt.hamming_loss(y_dis_pred, y_dis_true))

print(" jaccard距离：", mt.jaccard_similarity_score(y_dis_pred, y_dis_true))

# 回归
y_pred = [2.5, 0, 2, 8]
y_true = [3, -.5, 2, 7]

print("可释方差值", mt.explained_variance_score(y_true, y_pred))
print("平均绝对误值", mt.mean_absolute_error(y_true, y_pred))
print("均方误值", mt.mean_squared_error(y_true, y_pred))
print("中值绝对误值", mt.median_absolute_error(y_true, y_pred))
print("R方值", mt.r2_score(y_true, y_pred))






