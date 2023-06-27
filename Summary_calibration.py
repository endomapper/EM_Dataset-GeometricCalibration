import numpy as np
import sys
import os
import math
arg = sys.argv
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

x = np.linspace(0, 75.0*math.pi/180.0, num=1000)

i=0

for endoscope in arg[1:]:
	print(endoscope)
	root = ET.parse(endoscope).getroot()
	for type_tag in root.findall('camera/camera_model/params'):
	    x1, x2, x3, x4, x5, x6, x7, x8 = type_tag.text[2:-2].split(";")
	    print(type_tag.text[2:-2].split(";"))
	fx = []
	for n in range(len(x)):
	    fx.append((float(x5) * (float(x[n]) ** 3) + float(x6) * (float(x[n]) ** 5) + float(x7) * (float(x[n]) ** 7) + float(x8) * (float(x[n]) ** 9)+float(x[n])))
	plt.plot(x*180/math.pi,fx, label=endoscope.split("/")[0])
	i+=1
fx = []
for n in range(len(x)):
     fx.append(math.sin(float(x[n]))*1.0)
plt.plot(x*180/math.pi,fx,'--', label="Orthogonal_proyection")

fx = []
for n in range(len(x)):
    fx.append(2*math.sin(float(x[n])/2.0)*1.0)
plt.plot(x*180/math.pi,fx,'--', label="Equisolid_projection")

plt.xlabel(r"$\theta$ (deg)")
plt.ylabel(r"$r_d$ (mm)")
plt.legend(loc=0)
plt.grid()

plt.show()
