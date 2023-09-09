import numpy as np
import matplotlib.pyplot as plt

# plt.plot([1,2,3,4,5], [1, 4, 9, 16, 25])  # 선 그래프
# plt.scatter([1,2,3,4,5], [1, 4, 9, 16, 25]) # 산점도

x = np.random.randn(1000) # 난수 1000개
y = np.random.randn(1000)

plt.scatter(x, y)

plt.show()