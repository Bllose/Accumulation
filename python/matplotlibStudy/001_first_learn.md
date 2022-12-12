``` PYTHON
import matplotlib.pyplot as plt
# Numerical Python 支持大量的维度数组与矩阵运算， 也针对数组运算提供大量的数学函数
import numpy as np
# numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None)
# 在指定的间隔内返回均匀间隔的数字;
# 返回num均匀间隔的样本, 在[start，stop]区间内计算;
# 可以选择排除间隔的终点.
# stop: 当endpoint=True时，展示stop点；点endpoint=False时，不展示stop点
x = np.linspace(0, 2, 100)
in the following example, the first call to ```plt.plot```creates the axes, then subsequent calls to ```plt.plot``` add additional lines on the same axes, and ```plt.xlabel```,```plt.ylabel```, ```plt.title``` and ```plt.legend``` set the axes labels and title and add a legend.
``` Python
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()
## 日期相关图片
``` Python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
def price(x):
    return '$%1.2f' % x
def three():
    years = mdates.YearLocator() # every year
    months = mdates.MonthLocator()
    yearsFmt = mdates.DateFormatter('%Y')
    with cbook.get_sample_data('goog.npz') as datafile:
        r = np.load(datafile)['price_data'].view(np.recarray)
    fig, ax = plt.subplots()
    ax.plot(r.date, r.adj_close)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    datemin = np.datetime64(r.date[0], 'Y')
    datemax = np.datetime64(r.date[-1], 'Y') + np.timedelta64(1, 'Y')
    ax.set_xlim(datemin, datemax)
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.format_ydata = price
    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()
