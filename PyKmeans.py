#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入 python 科学计算和机器学习模块
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import Birch
from sklearn.cluster import KMeans

'''
    unmpy 是Python的科学计算包
    matplotlib 是Python的画图工具包
    scipy 是Python的科学工具集包
    scikit-learn 是Python的机器学习工具集包

numpy:
    主要用来做一些科学运算，主要是矩阵的运算。NumPy为Python带来了真正的多维数组功能，并且提供了丰富的函数库处理这些数组。
    它将常用的数学函数都进行数组化，使得这些数学函数能够直接对数组进行操作，将本来需要在Python级别进行的循环，放到C语言的
    运算中，明显地提高了程序的运算速度。
scipy:
    主要是一些科学工具集，信号处理工具集(如线性代数使用LAPACK库，快速傅立叶变换使用FFTPACK库)及数值计算的一些
    工具(常微分方程求解使用ODEPACK库，非线性方程组求解以及最小值求解等)
scikit-learn:
    里面有很多机器学习相关的算法(如聚类算法，SVM等);
    表示在sklearn中处理kmeans聚类问题，用到 sklearn.cluster.KMeans 这个类
    
matplotlib:
    是一个画图工具和Matlab中的画图工程类似;
    matplotlib.pyplot是用来画图的方法，matplotlib是可视化包
'''

# 创建输入数据
# D是数据集，包括2列20行，即20个球员的助攻数和得分数
D = [
    [0.0888, 0.5885],
    [0.1399, 0.8291],
    [0.0747, 0.4974],
    [0.0983, 0.5772],
    [0.1276, 0.5703],
    [0.1671, 0.5835],
    [0.1906, 0.5276],
    [0.1061, 0.5523],
    [0.2446, 0.4007],
    [0.1670, 0.4770],
    [0.2485, 0.4313],
    [0.1227, 0.4909],
    [0.1240, 0.5668],
    [0.1461, 0.5113],
    [0.2315, 0.3788],
    [0.0494, 0.5590],
    [0.1107, 0.4799],
    [0.2521, 0.5735],
    [0.1007, 0.6318],
    [0.1067, 0.4326],
    [0.1956, 0.4280]
]

# 打印数据
print(D)

# Kmeans 聚类
# 表示输出完整Kmeans函数，包括很多省略参数，将数据集分成类簇数为2的聚类
clf = KMeans(n_clusters=2)

# 输出聚类预测结果，对X聚类，20行数据，每个ypred对应X的一行或一个孩子，聚成2类，类标为0、1
ypred = clf.fit_predict(D)

# 输出结果
print(clf)
print(ypred)

'''
    获取第1列的值，使用for循环获取, n[0]表示X第1列
    获取第2列的值，使用for循环获取, n[1]表示X第2列
'''
x = [i[0] for i in D]
print(x)
y = [i[1] for i in D]
print(y)

# 可视化操作
'''
 绘制散点图(scatter)，
 横轴为x，获取的第1列数据
 纵轴为y，获取的第2列数据
 c = ypred 对聚类的预测结果画出散点图
 marker='*' 说明用点表示图形
'''
plt.scatter(x, y,
            c=ypred, marker='x')

# 图形的标题
plt.title("KmeansBaseketballData")

# 图形的x轴
plt.xlabel("assists_per_minute")

# 图形的y轴
plt.ylabel("points_per_minute")

# 图形右上角图例
plt.legend(["Rank"])

# 显示图形
plt.show()