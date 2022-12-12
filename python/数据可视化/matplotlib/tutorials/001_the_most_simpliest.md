一个可以执行的最简单样例
``` Python
import matplotlib.pyplot as plt
fig, ax = plt.subplots() # Create a figure containing a single axes.
ax.plot([1,2,3,4], [1,4,2,3])
plt.show()
使用```pyplot```创建一个**Figure**,是最简单的方法  
``` Python
fig = plt.figure() # 一个空的画布， 这意味着如果直接调用 plt.show()，你什么都看不到
fig, ax = plt.subplots()  # 拥有一张图表的画布
fig, axs = plt.subplots(2, 2) # 拥有4张图表的画布，并且这些图表成 2 x 2 网格结构
