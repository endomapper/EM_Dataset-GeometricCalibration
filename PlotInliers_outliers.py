import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import cv2
import sys


inliers = []
outliers = []
all= []
error = []
err_x = []
err_y = []
thre = 1.0


with open(sys.argv[1],'r') as fp:
    lines = fp.readlines()
    
n = 0
while not lines[n][0] == '_':
	n+=1
n+=1

for i in range(n,len(lines)):
    line= lines[i][:-1].split(":")
    x = float(line[0])
    y = float(line[1])
    errr=float(line[2])
    errx = float(line[3])
    erry = float(line[4])
    all.append((x,y))
    error.append(errr)
    err_x.append(errx)
    err_y.append(erry)

back = cv2.imread("background.jpg")
lower_black = np.array([2,2,2], dtype = "uint16")
upper_black = np.array([255,255,255], dtype = "uint16")
black_mask = cv2.inRange(back, lower_black, upper_black)
rect = patches.Rectangle((0,0),1440,1080,linewidth=2,edgecolor='r',facecolor='none')
fig, ax = plt.subplots()
ax.imshow(black_mask)
currentAxis = plt.gca()
currentAxis.add_patch(rect)

for j in range(len(err_x)):
    p = all[j]
    plt.plot((p[0],p[0]+err_x[j]*1),(p[1],p[1]+err_y[j]*1),color='green',linewidth=1)
    
plt.axis('equal')
plt.grid()
plt.savefig(sys.argv[2],dpi=800)
