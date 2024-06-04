import math

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle


def uklad(i):
    f = plt.figure()
    isqrt = int(math.sqrt(i))
    plt.axes(xlim=(0, i), ylim=(0, i), aspect='equal')
    for y in range(isqrt):
        for x in range(isqrt):
            atom = Circle((0.5*isqrt + x*isqrt, 0.5*isqrt + y*isqrt), radius=0.175*isqrt)
            f.gca().add_patch(atom)
    return f


def animate_instance(i):
    return None

if __name__ == '__main__':
    ani = animation.FuncAnimation(uklad(16), animate_instance, interval=100)
    plt.show()










