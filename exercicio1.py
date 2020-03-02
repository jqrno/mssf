import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import numpy as np


def x(t):
    return (2*(t**3)) - (10*(t**2)) - (30*t) + 50

def letra_a():
    xt = []
    for t in range (11):
        xt.append(x(t))
    s = pd.Series(xt)
    print(s)

def letra_b():
    t = np.linspace(0, 10, 100)
    plt.plot(t, x(t), label='linear')
    plt.xlabel('Tempo')
    plt.ylabel('Posição')
    plt.title("Posição em função do tempo")
    plt.legend()
    plt.show()
