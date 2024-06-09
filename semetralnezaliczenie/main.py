import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.patches import Circle

mass = 1
pot_depth = 1
sigma = 1
T = 2.5
dt = 0.00001
atoms = []
kb = 1.38064852e-23
atom_count = 16
cutoff_distance = 6

class Atom:
    def __init__(self, x, y, vx, vy, radius):
        self.position = np.array([x, y])
        self.velocity = np.array([vx, vy])
        self.circle = Circle((x, y), radius=radius)

    def update_velocity(self, velocity):
        self.velocity -= velocity

    def update_position(self):
        global dt
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
        self.circle.center = self.position

def uklad(i):
    global atoms
    global mass
    global kb
    fig = plt.figure()
    velocities = []
    isqrt = int(math.sqrt(i))
    plt.axes(xlim=(0, i), ylim=(0, i), aspect='equal')
    for y in range(isqrt):
        for x in range(isqrt):
            atom = Atom(0.5*isqrt + x*isqrt, 0.5*isqrt + y*isqrt, round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), 0.175*isqrt)
            fig.gca().add_patch(atom.circle)
            atoms.append(atom)
            velocities.append(atom.velocity)
    sum_velocity = np.sum(np.array(velocities), axis=0)
    for i, atom in enumerate(atoms):
        atom.velocity -= sum_velocity / len(velocities)
        print(f"Temperatura atomu {i + 1} wynosi: " + str((mass*np.linalg.norm(atom.velocity)**2)/3*kb) + " K")
    return fig


def animate_instance(frame):
    global dt
    global atoms
    global mass
    # Jako przyspieszanie obliczen uzylem metody hashmapy dla wartosci. Zmienia algorytm z O(n*(n-1)) w O((n*(n-1)/2)
    cache = {}
    verletList = {}
    for n in range(1000):
        if n % 10 == 0:
            verletList = {}
            for i, atom in enumerate(atoms):
                for j, atom_par in enumerate(atoms):
                    if (j, i) in verletList:
                        verletList[(i, j)] = verletList[(j, i)].copy()
                    else:
                        verletList[(i, j)] = np.linalg.norm(atom.position - atom_par.position) > cutoff_distance
        for i, atom in enumerate(atoms):
            sily = np.zeros((len(atoms), 2))
            for j, atom_par in enumerate(atoms):
                if verletList[(i, j)]:
                    continue
                else:
                    if atom_par is atom:
                        continue
                    if (i, j) in cache:
                        sily[j] = cache[(i, j)]
                        cache.pop((i, j))
                    else:
                        rij = atom.position - atom_par.position
                        dij = np.linalg.norm(rij)
                        sily[j] += 24 * rij / dij ** 2 * (2 * (1 / dij) ** 12 - (1 / dij) ** 6)
                        cache[(j, i)] = sily[j]
            atom.update_velocity(np.sum(sily, axis=0)/mass*dt)
            atom.update_position()
    return [atom.circle for atom in atoms]


if __name__ == '__main__':
    anim = animation.FuncAnimation(uklad(atom_count), animate_instance, frames=100, interval=50, blit=True)
    plt.show()