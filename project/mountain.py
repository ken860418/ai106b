from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def func(X, Y, x_move=0, y_move=0):
    def mul(X, Y, alis=1):
        return alis * np.exp(-(X * X + Y * Y))
    return mul(X, Y) + mul(X - x_move, Y - y_move, 2)
def show(X, Y):
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.meshgrid(X, Y)
    Z = func(X, Y, 1.7, 1.7)
    plt.title("demo_hill_climbing")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    plt.show()
if __name__ == '__main__':
    X = np.arange(-2, 4, 0.1)
    Y = np.arange(-2, 4, 0.1)
    show(X,Y)