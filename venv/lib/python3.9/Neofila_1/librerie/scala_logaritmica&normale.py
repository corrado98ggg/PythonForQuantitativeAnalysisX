import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 50)
    y = np.sin(3 ** x)
    z = np.cos(x)

    # passiamo qui tutti gli attributi
    fig, axes = plt.subplots(1, 2, figsize=(12, 4), dpi=100)

    axes[0].plot(x, x**2, x, np.exp(x))
    axes[0].set_title("scala tradizionale")
    axes[0].grid()

    axes[1].plot(x, x**2, x, np.exp(x))
    axes[1].set_yscale("log")
    axes[1].set_title("scala logaritmica (y)")
    axes[1].grid()

    plt.tight_layout()
    plt.show()
