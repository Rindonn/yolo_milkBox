
# # 假设这是原始的混淆矩阵，包含了 "background"
# confusion_matrix = np.array([
#     [0.99, 0.00, 0.00, 0.00, 0.00, 0.09],
#     [0.00, 0.96, 0.01, 0.00, 0.03, 0.36],
#     [0.01, 0.01, 0.99, 0.00, 0.00, 0.05],
#     [0.00, 0.00, 0.00, 1.00, 0.00, 0.18],
#     [0.00, 0.01, 0.00, 0.00, 0.97, 0.32],
#     [0.00, 0.01, 0.00, 0.00, 0.03, 0.00]
# ])

# 移除 'background' 对应的最后一行和最后一列

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 假设这是原始的混淆矩阵，包含了 "background"
confusion_matrix = np.array([
      [0.99, 0.00, 0.00, 0.00, 0.00, 0.09],
      [0.00, 0.96, 0.01, 0.00, 0.03, 0.36],
      [0.01, 0.01, 0.99, 0.00, 0.00, 0.05],
      [0.00, 0.00, 0.00, 1.00, 0.00, 0.18],
      [0.00, 0.01, 0.00, 0.00, 0.97, 0.32],
      [0.00, 0.01, 0.00, 0.00, 0.03, 0.00]
])

# 移除 'background' 对应的最后一行和最后一列
reduced_conf_matrix = np.delete(confusion_matrix, -1, axis=0)
reduced_conf_matrix = np.delete(reduced_conf_matrix, -1, axis=1)

# 将0替换为np.nan
reduced_conf_matrix = np.where(reduced_conf_matrix == 0, np.nan, reduced_conf_matrix)

# 类别名称，不包括 'background'
labels = ['Meiji', 'Morinaga', 'Hokkaido', 'Grapejuice', 'Yotsubateshibo']

# 使用 seaborn 绘制更新后的混淆矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(reduced_conf_matrix, annot=True, cmap='Blues', fmt=".2f", xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix')
plt.xlabel('True')
plt.ylabel('TruePredicted')
plt.show()


