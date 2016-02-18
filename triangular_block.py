import pySALESetup as pss
import numpy as np
import scipy.spatial as scsp
import scipy as sc
import random
import matplotlib.pyplot as plt
import time


X_cells    = 2000 
Y_cells    = 3000 
x_length   = 200.e-6
y_length   = 300.e-6
GRIDSPC    = x_length/X_cells
mat_no     = 3

pss.generate_mesh(X_cells,Y_cells,mat_no)
mats = pss.mats

r1 = np.array([0.,67.5])
r2 = np.array([100.,92.5])
r3 = np.array([200.,67.5])
r4 = np.array([300.,92.5])

r1 = r1[::-1]
r2 = r2[::-1]
r3 = r3[::-1]
r4 = r4[::-1]

r1 /= GRIDSPC*1.e6
r2 /= GRIDSPC*1.e6
r3 /= GRIDSPC*1.e6
r4 /= GRIDSPC*1.e6

pss.fill_above_line(r1,r2,mats[0],mixed=True)
pss.fill_above_line(r2,r3,mats[0],mixed=True)
pss.fill_above_line(r3,r4,mats[0],mixed=True)

pss.fill_plate(0.,300.,mats[1])

plt.figure()
plt.imshow(pss.materials[mats[0]-1],cmap='Greys',interpolation='nearest')
plt.show()
