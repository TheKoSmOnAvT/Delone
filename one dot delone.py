#!/usr/bin/env python
# coding: utf-8

# In[1]:


mas = [
    [0.0315979, 0.733747], [0.382188, 0.704233], [0.940343, 
  0.262746], [0.799569, 0.941558], [0.141168, 0.44017], [0.513709, 
  0.00948778], [0.757705, 0.24854], [0.864629, 0.703213], [0.602835, 
  0.879176], [0.302173, 0.0909703], [0.729263, 0.314024], [0.229358, 
  0.189478], [0.697666, 0.580277], [0.847169, 0.485246], [0.757323, 
  0.31753], [0.0476, 0.543687], [0.616154, 0.87736], [0.533891, 
  0.5342], [0.85845, 0.62882], [0.669262, 0.830986], [0.255615, 
  0.749644], [0.367088, 0.740016], [0.526352, 0.435621], [0.13773, 
  0.550538], [0.828686, 0.855344], [0.290561, 0.0652921], [0.0713635, 
  0.537814], [0.242961, 0.521605], [0.455209, 0.660454], [0.70907, 
  0.987405], [0.596759, 0.0316338], [0.0398082, 0.156419], [0.341144, 
  0.281989], [0.67272, 0.416403], [0.814792, 0.846369], [0.534989, 
  0.865865], [0.986106, 0.991025], [0.244428, 0.800573], [0.914743, 
  0.453211], [0.00146735, 0.278968], [0.459534, 0.792757], [0.292397, 
  0.291563], [0.862774, 0.761123], [0.252589, 0.135144], [0.52163, 
  0.479133], [0.57987, 0.718741], [0.706838, 0.632765], [0.0448802, 
  0.852876], [0.720732, 0.64174], [0.800452, 0.0523036], [0.805989, 
  0.188529], [0.798985, 0.773336], [0.346455, 0.395773], [0.506587, 
  0.481773], [0.483681, 0.63465], [0.253998, 0.346629], [0.96205, 
  0.155516], [0.674128, 0.627887], [0.255213, 0.522752], [0.629248, 
  0.775011], [0.534481, 0.881012], [0.828796, 0.722707], [0.728492, 
  0.692482], [0.0298117, 0.949371], [0.382037, 0.29671], [0.523225, 
  0.467599], [0.898357, 0.66206], [0.269227, 0.12097], [0.936306, 
  0.506544], [0.595099, 0.493083], [0.681094, 0.983792], [0.965851, 
  0.718073], [0.146613, 0.102781], [0.137054, 0.995366], [0.418121, 
  0.410298], [0.107243, 0.0459942], [0.0360833, 0.113589], [0.584018, 
  0.578395], [0.137727, 0.451529], [0.314791, 0.457425], [0.20142, 
  0.944985], [0.719693, 0.964342], [0.520326, 0.961193], [0.753842, 
  0.246269], [0.373713, 0.858412], [0.616788, 0.250904], [0.955593, 
  0.448114], [0.509545, 0.20491], [0.919509, 0.334525], [0.925527, 
  0.626514], [0.781783, 0.882996], [0.610736, 0.169089], [0.580363, 
  0.938011], [0.891043, 0.204747], [0.0600364, 0.976818], [0.137201, 
  0.958478], [0.686323, 0.118406], [0.520414, 0.707574], [0.73073, 
  0.670293], [0.0108688, 0.502664], [0.811221, 0.335768], [0.0853419, 
  0.87615], [0.029438, 0.452772], [0.474606, 0.707061], [0.449075, 
  0.514761], [0.583563, 0.502314], [0.389039, 0.537942], [0.446362, 
  0.543836], [0.702716, 0.419536], [0.925948, 0.836263], [0.971986, 
  0.749243], [0.915079, 0.333598], [0.160765, 0.413475], [0.829737, 
  0.457449], [0.131327, 0.960704], [0.355131, 0.750388], [0.682251, 
  0.445943], [0.771568, 0.248074], [0.293213, 0.908], [0.325207, 
  0.704237], [0.590497, 0.488464], [0.399259, 0.867975], [0.618511, 
  0.739221], [0.48418, 0.534376], [0.457746, 0.325746], [0.654442, 
  0.0769278], [0.32642, 0.365042], [0.299311, 0.32654], [0.644168, 
  0.919099], [0.527743, 0.0784664], [0.350956, 0.0110985], [0.202536, 
  0.374229], [0.760459, 0.522634], [0.803277, 0.506254], [0.141948, 
  0.783413], [0.319098, 0.971878], [0.684201, 0.457668], [0.664655, 
  0.89495], [0.357782, 0.0926256], [0.365344, 0.56841], [0.713614, 
  0.173527], [0.837601, 0.489944], [0.362658, 0.162428], [0.635065, 
  0.115714], [0.602199, 0.639794], [0.831787, 0.60946], [0.460252, 
  0.856381], [0.51269, 0.637582], [0.77605, 0.398713], [0.848034, 
  0.742632], [0.418268, 0.306088], [0.48269, 0.174222], [0.704654, 
  0.132561], [0.645089, 0.684279], [0.341996, 0.970133], [0.0100246, 
  0.568564], [0.739797, 0.330339], [0.178237, 0.959104], [0.279545, 
  0.473958], [0.665548, 0.321522], [0.503495, 0.0752446], [0.817513, 
  0.578889], [0.0852271, 0.769157], [0.334823, 0.404667], [0.380573, 
  0.636596], [0.689734, 0.720389], [0.0385765, 0.666463], [0.679709, 
  0.151825], [0.29878, 0.336124], [0.501472, 0.192721], [0.0192344, 
  0.862166], [0.835924, 0.8712], [0.515739, 0.786921], [0.0184108, 
  0.29231], [0.430512, 0.0177644], [0.683588, 0.887643], [0.0499394, 
  0.381169], [0.993854, 0.167254], [0.0113628, 0.714706], [0.314145, 
  0.0154289], [0.712583, 0.378582], [0.812674, 0.822708], [0.693349, 
  0.516416], [0.97675, 0.951508], [0.17761, 0.729495], [0.958339, 
  0.659198], [0.747098, 0.711731], [0.274751, 0.771556], [0.697158, 
  0.330562], [0.280897, 0.604302], [0.685795, 0.615856], [0.966751, 
  0.588873], [0.973212, 0.237274], [0.154078, 0.766165], [0.279864, 
  0.720858], [0.177328, 0.814657], [0.102254, 0.991363], [0.218989, 
  0.155458], [0.355156, 0.279632], [0.944238, 0.383903]
]


# In[2]:


import numpy as np
import math
import matplotlib.pyplot as plt
import random

mainDotIndex = 100 - 15#random.randint(1, 99) #100 - 12 #random.randint(1, 99) 
mainDot = mas[mainDotIndex]


# In[3]:


q1 = []
q2 = []
q3 = []
q4 = []

xp = []
xm = []
yp = []
ym = []


# In[4]:


#Разбиваем на сектора
for i in range(0, len(mas)):
    if mainDotIndex == i:
        continue
    tempX = mas[i][0] - mas[mainDotIndex][0]
    tempY = mas[i][1] - mas[mainDotIndex][1]
    
    if tempX > 0 and tempY == 0:
        xp.append(i)
    if tempX < 0 and tempY == 0:
        xm.append(i)
    if tempY > 0 and tempX == 0:
        yp.append(i)
    if tempY < 0 and tempX == 0:
        ym.append(i)
        
    if tempX > 0 and tempY > 0:
        q1.append(i)
    if tempX < 0 and tempY > 0:
        q2.append(i)
    if tempX < 0 and tempY < 0:
        q3.append(i)
    if tempX > 0 and tempY < 0:
        q4.append(i)


# In[5]:


xpb = {x: (mas[x][0] - mas[mainDotIndex][0]) for x in xp }
xmb =  {x: ( mas[x][0] - mas[mainDotIndex][0]) for x in xm}
ypb =  {x: ( mas[x][1] - mas[mainDotIndex][1]) for x in yp}
ymb = {x: ( mas[x][1] - mas[mainDotIndex][1]) for x in ym}

#подсчет угла
q1b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q1}
q2b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q2}
q3b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q3}
q4b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q4}


# In[6]:


#функция для отображения последовательности точек 
def renderingOrders(dot, mas):    
    fig = plt.figure()
    ax = fig.add_subplot()
    index = 0
    plt.scatter([mainDot[0]],[mainDot[1]] , c="purple")
    for dot in dot:
        plt.text(mas[dot][0] ,mas[dot][1], str(index), fontsize=10)
        plt.scatter(mas[dot][0],mas[dot][1], c="r")
        index+=1
    
    plt.grid()
    plt.show()

#отображение деления областей
def renderDivisions(q1,q2,q3,q4):
    plt.figure(figsize=(10, 10)) 
    plt.scatter(mas[mainDotIndex][0], mas[mainDotIndex][1], color='purple')

    for i in range(0,len(q1b)):
        plt.scatter(mas[q1b[i]][0], mas[q1b[i]][1], color='green')
    for i in range(0,len(q2b)):
        plt.scatter(mas[q2b[i]][0], mas[q2b[i]][1], color='red')    
    for i in range(0,len(q3b)):
        plt.scatter(mas[q3b[i]][0], mas[q3b[i]][1], color='black')      
    for i in range(0,len(q4b)):
        plt.scatter(mas[q4b[i]][0], mas[q4b[i]][1], color='brown')

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    


# In[7]:


#сортировка
q1b = {k: v for k, v in sorted(q1b.items(), key=lambda item: item[1] )} 
q2b = {k: v for k, v in sorted(q2b.items(), key=lambda item: item[1], reverse=True )}
q3b = {k: v for k, v in sorted(q3b.items(), key=lambda item: item[1])}
q4b = {k: v for k, v in sorted(q4b.items(), key=lambda item: item[1], reverse=True)}

#отображение последовательности
renderingOrders(q1b,mas)
renderingOrders(q2b,mas)
renderingOrders(q3b,mas)
renderingOrders(q4b,mas)

#преобр словаря в лист ключей
q1b = list(q1b.keys())
q2b = list(q2b.keys())
q3b = list(q3b.keys())
q4b = list(q4b.keys())
xpb = list(xpb.keys())
xmb = list(xmb.keys())
ypb = list(ypb.keys())
ymb = list(ymb.keys())

#отображение деления областей
renderDivisions(q1b,q2b,q3b,q4b)


# In[8]:


#функция получения параметров окружности
def getCircle(dot1, dot2, dot3):
    A = dot2[0] - dot1[0]
    B = dot2[1] - dot1[1]
    C = dot3[0] - dot1[0]
    D = dot3[1] - dot1[1]
    E = A * (dot1[0] + dot2[0]) + B * (dot1[1] + dot2[1])
    F = C * (dot1[0] + dot3[0]) + D * (dot1[1] + dot3[1])
    G = 2 * (A * (dot3[1] - dot2[1]) - B * (dot3[0] - dot2[0]))
    
    if (G == 0):
        return []
    
    #координаты центра
    Cx = (D * E - B * F) / G
    Cy = (A * F - C * E) / G
    #радиус
    R = math.sqrt(math.pow(dot1[0] - Cx, 2) + math.pow(dot1[1] - Cy, 2))
   
    return [Cx, Cy, R]


# In[9]:


#проверка условия делоне
def checkDelone(circleParam, dot, mas):
    if ((mas[dot][0]-circleParam[0])**2 + (mas[dot][1]-circleParam[1])**2 < circleParam[2]**2):
        return False
    return True


# In[10]:


#получение отсорт. массива точек для отрисовки 
def getCoords(arrayIdsDots, mas, mainDotIndex):
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    
    for i in arrayIdsDots:
        tempX = mas[i][0] - mas[mainDotIndex][0]
        tempY = mas[i][1] - mas[mainDotIndex][1]

        if tempX > 0 and tempY == 0:
            xp.append(i)
        if tempX < 0 and tempY == 0:
            xm.append(i)
        if tempY > 0 and tempX == 0:
            yp.append(i)
        if tempY < 0 and tempX == 0:
            ym.append(i)

        if tempX > 0 and tempY > 0:
            q1.append(i)
        if tempX < 0 and tempY > 0:
            q2.append(i)
        if tempX < 0 and tempY < 0:
            q3.append(i)
        if tempX > 0 and tempY < 0:
            q4.append(i)
    
    
    q1b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q1}
    q2b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q2}
    q3b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q3}
    q4b = {x: np.arcsin((math.sqrt((mas[mainDotIndex][1]-mas[x][1])**2))/math.sqrt((mas[mainDotIndex][0]-mas[x][0])**2 + (mas[mainDotIndex][1]-mas[x][1])**2)) for x in q4}
    q1b = {k: v for k, v in sorted(q1b.items(), key=lambda item: item[1] )} 
    q2b = {k: v for k, v in sorted(q2b.items(), key=lambda item: item[1], reverse=True )}
    q3b = {k: v for k, v in sorted(q3b.items(), key=lambda item: item[1])}
    q4b = {k: v for k, v in sorted(q4b.items(), key=lambda item: item[1], reverse=True)}
    q1b = list(q1b.keys())
    q2b = list(q2b.keys())
    q3b = list(q3b.keys())
    q4b = list(q4b.keys())
    
    
    arrayDots = []
    for i in (q1+q2+q3+q4):
        arrayDots.append(mas[i])        
    return arrayDots


# In[11]:


#получение точек, которые удовл делоне
def getDots(mas, mainDotIndex, dots):   
    dotsIndexArray = dots[1:]
    lenght = len(dotsIndexArray)
    step = 3
    checkEqual = []
    while not np.array_equal(dotsIndexArray, checkEqual):
        checkEqual = dotsIndexArray
        while step < lenght and  lenght > 3:
            circle = getCircle(mas[mainDotIndex], mas[dotsIndexArray[step-2]], mas[dotsIndexArray[step-1]])
            if not checkDelone(circle, dotsIndexArray[step], mas):
                if step == 0:
                      dotsIndexArray =  dotsIndexArray[step:-1]
                else: 
                      dotsIndexArray = np.concatenate((dotsIndexArray[:step-1], dotsIndexArray[step:]))
                step -= 1
                lenght -= 1
            step += 1
        step = 0
    return dotsIndexArray


# In[12]:


def drawDelone(mainDot, dots):    
    fig = plt.figure()
    ax = fig.add_subplot()
    for dot in range(0,len(dots)):
        plt.scatter(dots[dot][0],dots[dot][1], c="r")  
        plt.plot([dots[dot][0],mainDot[0]],[dots[dot][1],mainDot[1]], color='blue')
        if(dot != len(dots)-1):
            plt.plot([dots[dot][0],dots[dot+1][0]],[dots[dot][1],dots[dot+1][1]], color='blue')

    plt.plot([dots[0][0],dots[len(dots)-1][0]],[dots[0][1],dots[len(dots)-1][1]], color='blue')
    plt.scatter([mainDot[0]],[mainDot[1]] , c="purple")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.figure.set_size_inches(10, 10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.grid()


# In[13]:


dotsIdsCoord = list(getDots(mas, mainDotIndex,q1b+q2b+q3b+q4b)) 
dots = getCoords(dotsIdsCoord, mas, mainDotIndex)
drawDelone(mainDot, dots)


# In[ ]:




