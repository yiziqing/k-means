#-*- coding: UTF-8 -*-

import random
import math

'''
1，造数据，展示数据

2，计算距离，这里用的是欧式距离，当然其他合理的距离都是可以的

3，随机生成初始的K

4,keans算法，输入数据和k值

5，展示聚类之后的数据
'''

'''坐标类'''
class Coordinate:

    def __init__(self,x,y,k,flag):
        self.x=x
        self.y=y
        self.k=k #聚类类型
        self.flag=flag #1，聚类中心标识

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.flag=0



'''获取随机数'''
def getRandom():
    return random.randint(0,100)

#random.uniform(1,50)

'''创建坐标集合'''
def createCoordinateList():
    list=[]
    for num in range(0,30):
        list.append(Coordinate(num,getRandom()))

    '''展示坐标信息'''
    list.sort(cmp=None, key=lambda x:x.x, reverse=True)
    for obj in list:
        print ' '*(obj.y-1)+'*'

    print ''
    print '='*110
    return list

#print list.count('90')

'''计算距离（欧式距离）'''
def distEuclid(coordinateA,coordinateB):
    return math.sqrt(pow((coordinateA.x-coordinateB.x),2)+pow((coordinateA.y-coordinateB.y),2))

'''随机选取K'''
def randomK(list,k):
    listK=[]
    listRandom=[]
    for l in range(0,k):
        num=randomNum(listRandom,random.randint(0,len(list)-1),list)
        coordinate=list[num]
        coordinate.k=l
        coordinate.flag=1
        list[num].flag=1
        listK.append(coordinate)
        listRandom.append(num)
    return listK

'''递归，防止选取重复K'''
def randomNum(listRandom,num,list):
    if(listRandom.count(num)<=0):
        return num
    else:
        num=random.randint(0,len(list)-1)
        return randomNum(listRandom,num,list)

'''kmeans算法，输入数据和k值'''
def kMeans(data,k,deep):
    listK=randomK(data,k)
    clusterData(data,listK)
    distNewK(data,k,deep,0)
    return data

def clusterData(data,listK):
    for l in data:
        kValue=distValue=count=0
        for key in listK:
            value=distEuclid(l,key)
            if(count==0):
                distValue=value
                kValue=key.k
                count=count+1
                continue
            if(value<distValue):
                distValue=value
                kValue=key.k
        l.k=kValue
    showData(data,len(listK))
    return data


'''所有数减去其平均值的平方和，所得结果除以该组数之个数（或个数减一，即变异数），再把所得值开根号，所得之数就是这组数据的标准差。'''
'''质心算法
在很多应用中，需要对某个目标进行定位。比如对于一个未知坐标的点A，假定已知A点与N个点相邻，且已知N个相邻点的坐标，则可取N个点的质心作为A点坐标的一个估计值。
所谓质心，就是指其横坐标、纵坐标分别为N个点的横坐标平均值、纵坐标平均值的点。即：假定N个点的坐标分别（x1,y1)，(x2,y2)，......，则质心的坐标为（(x1+x2+...)/N, (y1+y2+...)/N)。
'''

'''选取聚类中距质心最近的坐标为新的K'''
def distNewK(data,k,deep,num):
    num=num+1
    listK=[]
    result=0
    for key in range(0,k):
        newKValue=0
        yValue=xValue=count=0
        for l in data:
            if(key==l.k):
                xValue=xValue+l.x
                yValue=yValue+l.y
                count=count+1
        newCoordinate=Coordinate(xValue/count,yValue/count)

        index=record=distValue=count=flagKIndex=0

        for l in data:
            if(l.k==key):
                if(l.flag==1):
                    flagKIndex=index
                value=distEuclid(newCoordinate,l)
                if(count==0):
                    distValue=value
                    record=index
                    count=count+1
                if(distValue>value):
                    distValue=value
                    record=index
            index=index+1

        if(flagKIndex!=record):
            data[record].flag=1
            data[flagKIndex].flag=0
            result=1
        listK.append(data[record])

    if(result==1):
        clusterData(data,listK)
        if(num<=deep):
            distNewK(data,k,deep,num)

'''展示聚类后的结果'''
# def showData(data,k):
#     for obj in data:
#         value=''
#         if(obj.flag==1):
#             value=' '*(obj.y-1)+'#'
#         else:
#             value=' '*(obj.y-1)+'*'
#         if(obj.k==0):
#             print('\033[0;31m%s\033[0m' % value)
#         elif(obj.k==1):
#             print('\033[0;34m%s\033[0m' % value)
#         elif(obj.k==2):
#             print('\033[0;32m%s\033[0m' % value)
#         elif(obj.k==3):
#             print('\033[0;36m%s\033[0m' % value)
#         elif(obj.k==4):
#             print('\033[0;35m%s\033[0m' % value)
#     print '='*110


def showData(data,k):
    for obj in data:
        if(obj.k==0):
            if(obj.flag==1):
                print ' '*(obj.y-1)+'A'
            else:
                print(' '*(obj.y-1)+'a')
        if(obj.k==1):
            if(obj.flag==1):
                print ' '*(obj.y-1)+'B'
            else:
                print(' '*(obj.y-1)+'b')
        if(obj.k==2):
            if(obj.flag==1):
                print ' '*(obj.y-1)+'C'
            else:
                print(' '*(obj.y-1)+'c')
        if(obj.k==3):
            if(obj.flag==1):
                print ' '*(obj.y-1)+'D'
            else:
                print(' '*(obj.y-1)+'d')
        if(obj.k==4):
            if(obj.flag==1):
                print ' '*(obj.y-1)+'E'
            else:
                print(' '*(obj.y-1)+'e')
        if(obj.k==5):
            if(obj.flag==1):
                print ' '*(obj.y-1)+'F'
            else:
                print(' '*(obj.y-1)+'f')
    print '='*110

def main():
    # showData(list,3,5)
    kMeans(createCoordinateList(),4,50)

if __name__ == '__main__':
    main()















