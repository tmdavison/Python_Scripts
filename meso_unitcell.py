import numpy as np
import scipy.spatial as scsp
import scipy as sc
import random
import matplotlib.pyplot as plt
import pySALESetup as pss
import time


vol_frac   = .55
X_cells    = 500 
Y_cells    = 500 
PR         = 0.
cppr       = 8 
vfraclimit = .495                               # The changeover point from random to forced contacts. > 1.0 => least contacts; = 0. Max contacts
x_length   = 1.e-3
y_length   = 1.e-3
GRIDSPC    = x_length/X_cells
mat_no     = 5

pss.generate_mesh(X_cells,Y_cells,mat_no,cppr,PR,vol_frac)
mats = pss.mats

part_area  = np.zeros((1))
cppr_range = pss.cppr_max - pss.cppr_min
r = pss.cppr_mid
pss.mesh_Shps[0,:,:],part_area[0] = pss.gen_circle(r)

lx, ly = 64, 64
UC = pss.unit_cell(LX=lx,LY=ly)

pss.place_shape(pss.mesh_Shps[0,:,:],0,0,1,UC,LX=lx,LY=ly)
pss.place_shape(pss.mesh_Shps[0,:,:],48,32+16,2,UC,LX=lx,LY=ly)
pss.place_shape(pss.mesh_Shps[0,:,:],32,32-20,3,UC,LX=lx,LY=ly)
pss.place_shape(pss.mesh_Shps[0,:,:],48,32-16,4,UC,LX=lx,LY=ly)
pss.place_shape(pss.mesh_Shps[0,:,:],32,32+20,1,UC,LX=lx,LY=ly)


pss.place_shape(pss.mesh_Shps[0,:,:],lx,0,1,UC,LX=lx,LY=ly)
pss.place_shape(pss.mesh_Shps[0,:,:],0,ly,1,UC,LX=lx,LY=ly)
pss.place_shape(pss.mesh_Shps[0,:,:],lx,ly,1,UC,LX=lx,LY=ly)



plt.figure()
plt.imshow(UC[0,:,:],interpolation='nearest',cmap='binary')
plt.imshow(UC[1,:,:],interpolation='nearest',cmap='binary',alpha=.5)
plt.imshow(UC[2,:,:],interpolation='nearest',cmap='binary',alpha=.5)
plt.imshow(UC[3,:,:],interpolation='nearest',cmap='binary',alpha=.5)

pss.copypasteUC(UC)

plt.figure()
plt.imshow(pss.materials[0,:,:],interpolation='nearest',cmap='binary')
plt.imshow(pss.materials[1,:,:],interpolation='nearest',cmap='binary',alpha=.5)
plt.imshow(pss.materials[2,:,:],interpolation='nearest',cmap='binary',alpha=.5)
plt.imshow(pss.materials[3,:,:],interpolation='nearest',cmap='binary',alpha=.5)
plt.show()

S = float(np.sum(UC)-4*3)#There are 4 particles and 3 cells overlap per particle
print "Approximate Volume Fraction = {:3.1f}".format(S/float(lx*ly))

pss.save_general_mesh(mixed=False)


