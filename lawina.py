import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig = plt.figure()
N = 101
czas = 5000
z = np.zeros((N, N))
stos = []
coile = 1
xsr = int(N / 2)
ysr = int(N / 2)
trace = {}
for it in range(0, czas):
    lawina_size = 0
    lawina_index = set()
    z[xsr][ysr] += 1
    if z[xsr][ysr] > 4:
        stos.append([xsr, ysr])
    while stos:
        x = stos[-1][0]
        y = stos[-1][1]
        if (x, y) not in lawina_index:
            lawina_size += 1
            lawina_index.add((x, y))

        z[x][y] -= 4
        if x + 1 < N:
            z[x + 1][y] += 1
        if x > 0:
            z[x - 1][y] += 1
        if y + 1 < N:
            z[x][y + 1] += 1
        if y > 0:
            z[x][y - 1] += 1
        if z[x][y] <= 4:
            stos.pop()

        if x + 1 < N and z[x + 1][y] > 4 and ([x + 1, y] not in stos):
            stos.append([x + 1, y])
        if x > 0 and z[x - 1][y] > 4 and ([x - 1, y] not in stos):
            stos.append([x - 1, y])
        if y + 1 < N and z[x][y + 1] > 4 and ([x, y + 1] not in stos):
            stos.append([x, y + 1])
        if y > 0 and z[x][y - 1] > 4 and ([x, y - 1] not in stos):
            stos.append([x, y - 1])
    if lawina_size != 0:
        if lawina_size in trace:
            trace[lawina_size] += 1
        else:
            trace[lawina_size] = 1
    # if it % coile == 0:
    #     nStr = str(it)
    #     nStr = nStr.rjust(6,'0')
    #     ax = fig.add_subplot(111)
    #     ax.set_title('Height of the Sandpile')
    #     cax = ax.imshow(z, interpolation='nearest')
    #     cax.set_clim(vmin=0, vmax=6)
    #     cbar = fig.colorbar(cax, ticks=[0,2,4], orientation='vertical')
    #     fig.savefig('Ewolucja'+nStr+'.png')
    #     plt.clf()
x, y = zip(*sorted(trace.items()))
slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(x),np.log(y))
y_pred = np.exp(slope * np.log(np.array(x)) + intercept)
plt.plot(x, y, linestyle='none', marker='o')
plt.plot(x, y_pred, color='red', label=f'Linia: y = {slope:.2f}x + {intercept:.2f}')
plt.xscale('log')
plt.yscale('log')
plt.show()
# przyciac dla wszystkich x < 100