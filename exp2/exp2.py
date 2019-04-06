'''

Auther:     王子翔
Class:      计算机科学与技术17-1班
ID:         2017217713
FileName:   exp2.py
Date:       2019.04.06

'''

# coding:utf-8

import os
import math


class Intersect:
    def ins_line(self, k0, b0, k1, b1):
        if k0 == k1:
            print("两直线平行不相交!")
            return -1
        else:
            x = float((b1-b0)/(k0-k1))
            y = float(k0*x+b0)
            print("两直线交点为(%f,%f)" % (x, y))
            return 0

    def ins_circle(self, k0, b0, a, b, r):
        d = float((k0*a-b+b0)/math.sqrt(k0 * k0 + 1))
        if d > r:
            print("直线与圆相离!")
            return -1
        elif d == r:
            x = float(-1 * (b0 - b - a / k0) / (k + 1 / k))
            y = float(k0 * x + b0)
            print("直线和圆的交点为(%f,%f)" % (x, y))
            return 0
        else:
            # x_mid, y_mid为交点中点坐标
            x_mid = float(-1 * (b0 - b - a / k0) / (k + 1 / k))
            y_mid = float(k0 * x + b0)
            # dist为交线段半长
            dist = float(math.sqrt(r * r - d * d))
            # arc为k0倾角
            arc = float(math.atan(k0))
            # delta为增量
            delta_x = float(math.cos(arc)*dist)
            delta_y = float(math.sin(arc)*dist)
            x0 = float(x_mid - delta_x)
            y0 = float(y_mid - delta_y)
            x1 = float(x_mid + delta_x)
            y1 = float(y_mid + delta_y)
            print("直线和圆的交点为(%f,%f), (%f,%f)" % (x0, y0, x1, y1))
            return 0

    def ins_rectangle(self, k, b, x1, y1, x2, y2, x3, y3, x4, y4):
        # 求出四个顶点构成的界限
        # 矩形只需要两个k即可, 计算4个k可以求所有的四边形
        k_lf = float((y1-y4)/(x1-x4))
        k_up = float((y1-y2)/(x1-x2))
        k_rg = float((y2-y3)/(x2-x3))
        k_bl = float((y3-y4)/(x3-x4))

        b_lf = float(y1 - k_lf * x1)
        b_up = float(y2 - k_up * x2)
        b_rg = float(y3 - k_rg * x3)
        b_bl = float(y4 - k_bl * x4)

        # 比较四条边交点
        if k != k_lf:
            x = float((b - b_lf) / (k - k_lf))
            y = float(k * x + b)
            if x >= min(x1, x4) & x <= max(x1, x4):
                print("直线和矩形交点为(%f,%f)" % (x, y))
        if k != k_up:
            x = float((b - b_up) / (k - k_up))
            y = float(k * x + b)
            if x >= min(x1, x2) & x <= max(x1, x2):
                print("直线和矩形交点为(%f,%f)" % (x, y))
        if k != k_rg:
            x = float((b - b_rg) / (k - k_rg))
            y = float(k * x + b)
            if x >= min(x2, x3) & x <= max(x2, x3):
                print("直线和矩形交点为(%f,%f)" % (x, y))
        if k != k_bl:
            x = float((b - b_bl) / (k - k_bl))
            y = float(k * x + b)
            if x >= min(x3, x4) & x <= max(x3, x4):
                print("直线和矩形交点为(%f,%f)" % (x, y))
        return 0


if __name__ == '__main__':
    print("Start Running..              exp2 - 求交点问题")
    print("0. 求直线相交请请按照y=kx+b格式输入line1 & line2的[4]个参数")
    print("1. 求直线和圆相交请按照y=kx+b格式和(X-A)^2+(Y-B)^2=r^2格式输入[5]个参数")
    print("2. 求直线和矩形交点请按照y=kx+b格式和矩阵四个顶点(x, y)输入[10]个参数")
    print("------------------------------------------------------------------------------")

    par = []
    inp = float(input("请输入参数(输入9999退出):"))
    par_num = 0

    while(inp != 9999):
        par.append(inp)
        par_num = par_num + 1
        inp = float(input("请输入参数(输入9999退出):"))

    if par_num < 4 | par_num>6:
        print("参数错误!")
    elif par_num == 4:
        inc = Intersect()
        inc.ins_line(par[0], par[1], par[2], par[3])
    elif par_num == 5:
        inc = Intersect()
        inc.ins_circle(par[0], par[1], par[2], par[3], par[4])
    else:
        inc = Intersect()
        inc.ins_rectangle(par[0], par[1], par[2], par[3], par[4], par[5], par[6], par[7], par[8])

    print("\n程序结束!")
    os.system("pause")