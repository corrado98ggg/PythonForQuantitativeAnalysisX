import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(0, 2* np.pi, 50)
    y = np.sin(4**x)
    z = np.cos(x)

    #passiamo qui tutti gli attributi
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4), dpi=100)

    for ax in axes:
        ax.plot(x,y,x,z,"blue")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('funzioni')
        ax.grid()

    plt.tight_layout()
    plt.show()


