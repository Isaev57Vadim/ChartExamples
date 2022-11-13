import matplotlib.pyplot as plt
import numpy as np

def plot_chart():

    # Данные для графика
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.cos(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='График косинуса matplotlib')
    ax.grid()

    plt.show()
