import cv2
import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib.patches as patches
import sys
import math
import xml.etree.ElementTree as ET


divej2 = 1

colos = np.linspace(170,1320,10)
rowos = np.linspace(100,990,10)

names = sys.argv[1:]
color = ['red','blue','green','black','orange','magenta','yellow','brown','grey','cyan']


x = [255,1234,1420,1420,1234,255,70,70,255]
y = [0,0,220,860,1080,1080,860,220,0]
xx = [0,1440,1440,0,0]
yy = [0,0,1080,1080,0]

plt.plot(x,y,linewidth=1,color='black')
plt.plot(xx,yy,linewidth=1,color='black')
for i in rowos:
    rows = [(j * divej2, i) for j in range(int(170 / divej2)+1, int(1320 / divej2)+1)]
    plt_x = [k[0] for k in rows]
    plt_y = [k[1] for k in rows]
    plt.plot(plt_x, plt_y, linewidth = 3,color='slateblue',label='original_grid')
for i in colos:
    cols = [(i,j*divej2) for j in range(int(100 / divej2)+1,int(990/divej2)+1)]
    plt_x = [k[0] for k in cols]
    plt_y = [k[1] for k in cols]
    plt.plot(plt_x, plt_y,  linewidth = 2,color='slateblue',label='original_grid')

for endoscopes in range(len(names)):
    print(names[endoscopes])
    root = ET.parse(names[endoscopes]).getroot()

    for type_tag in root.findall('camera/camera_model/params'):

        x1,x2,x3,x4,x5,x6,x7,x8 = type_tag.text[2:-2].split(";")

    dist = np.array([ float(x5), float(x6),float(x7),float(x8)]).reshape((4,1))
    mtx =  np.array([[float(x1), 0.0, float(x3)],
                     [0.0, float(x2), float(x4)],
                     [0.0, 0.0, 1.0]])
    for i in rowos:
        rows = [(j*divej2,i) for j in range(int(170 / divej2)+1, int(1320 / divej2)+1)]
        X = np.array(rows, dtype=np.float32).reshape((len(rows), 1, 2))
        X2 = cv2.fisheye.undistortPoints(X,mtx,dist,P=mtx)
        X2 = [x for x in X2]
        plt_x = [k[0,0] for k in X2]
        plt_y = [k[0,1] for k in X2]
        plt.plot(plt_x, plt_y, color=color[endoscopes],  label=names[endoscopes].split("/")[0])
        
    for i in colos:
        cols = [(i,j*divej2) for j in range(int(100 / divej2)+1,int(990/divej2)+1)]
        X = np.array(cols, dtype=np.float32).reshape((len(cols), 1, 2))
        X2 = cv2.fisheye.undistortPoints(X,mtx,dist,P=mtx)
        X2 = [x for x in X2]
        plt_x = [k[0,0] for k in X2]
        plt_y = [k[0,1] for k in X2]
        plt.plot(plt_x, plt_y, color=color[mm],  label=names[mm].split("/")[0])
        
plt.minorticks_on()
plt.grid(which='both',linewidth=0.5)
plt.axis('equal')
plt.xlabel('pix')
plt.ylabel('pix')
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(),loc='upper center',prop={'size': 6})
plt.gca().invert_yaxis()
plt.xlim([-600,2100])
plt.ylim([-500,1800])
plt.tight_layout()
plt.show()

