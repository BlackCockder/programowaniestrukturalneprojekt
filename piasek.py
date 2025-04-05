#!/usr/bin/env python
import sys
import random
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
N = 25
czas = 2500
z = np.zeros((N, N))
stos = []
coile = 1
xsr = int(N/2)
ysr = int(N/2)
for it in range(0, czas):
    z[xsr][ysr] += 1
    if z[xsr][ysr] > 4:
        stos.append([xsr, ysr])
    while stos:
        index = len(stos) - 1
        print(str(it) + ":" + str(index))
        x = stos[index][0]
        y = stos[index][1]

        z[x][y] -= 4
        if x + 1 < N:
            z[x + 1][y] += 1 
        if x - 1 < N and x >= 0:
            z[x - 1][y] += 1
        if y + 1 < N:
            z[x][y + 1] += 1
        if y - 1 < N and y >= 0:
            z[x][y - 1] += 1
        stos.pop(index)

        if x + 1 < N and z[x + 1][y] > 4 and ([x + 1, y] not in stos):
            stos.append([x + 1, y])
        if x - 1 < N and x >= 0 and z[x - 1][y] > 4 and ([x - 1, y] not in stos):
            stos.append([x - 1, y])
        if y + 1 < N and z[x][y + 1] > 4 and ([x, y + 1] not in stos):
            stos.append([x, y + 1])
        if y - 1 < N and y >= 0 and z[x][y - 1] > 4 and ([x, y - 1] not in stos):
            stos.append([x, y - 1])
        
    if it % coile == 0:
        nStr = str(it)
        nStr = nStr.rjust(6,'0')
        ax = fig.add_subplot(111)
        ax.set_title('Height of the Sandpile')
        cax = ax.imshow(z, interpolation='nearest')
        cax.set_clim(vmin=0, vmax=6)
        cbar = fig.colorbar(cax, ticks=[0,2,4], orientation='vertical')
        fig.savefig('Ewolucja'+nStr+'.png')
        plt.clf()
