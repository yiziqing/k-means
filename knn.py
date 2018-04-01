#-*- coding: UTF-8 -*-

import kmeans

def knnMethod(data,newCoordinate,type):

    for obj in data:
        #计算集合中每个坐标与新增加的坐标的距离
        obj.distance=kmeans.distEuclid(obj,newCoordinate)

    #集合根据计算出的距离排序
    data.sort(cmp=None, key=lambda x:x.distance, reverse=False)

    c=0
    for obj in data:
        if(c>=type):
            break
        print '距离最近的k是：'+str(obj.k)
        c=c+1

    preTotalCount=0
    key=0
    for num in range(0,type):
        count=0
        currentCount=0
        for obj in data:
            if(count<type):
                if(obj.k==num):
                    currentCount=currentCount+1
            else:
                break;
            count=count+1

        if(currentCount>preTotalCount):
            preTotalCount=currentCount
            key=num
    print '新增加的坐标的聚类为：'+str(key)
    print '='*110

    newCoordinate.k=key
    data.append(newCoordinate)
    data.sort(cmp=None, key=lambda x:x.x, reverse=True)
    kmeans.showData(data,type)

def main():
    type=4

    data=kmeans.kMeans(kmeans.createCoordinateList(),type,50)

    newCoordinate=kmeans.Coordinate(10,68)
    #增加的坐标标识
    newCoordinate.increFlag=1
    knnMethod(data,newCoordinate,type)

if __name__ == '__main__':
    main()