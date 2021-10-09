import matplotlib
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dado1 = np.random.randint(1, 7, 1000)
    dado2 = np.random.randint(1, 7, 1000)

    bins = 11  # la somma di due dadi a sei facce va da 2 a 12!

    plt.figure(figsize=(8, 4), dpi=100)
    plt.hist(dado1 + dado2, bins, color="green")
    plt.xlabel('somma')
    plt.ylabel('occorrenze')
    plt.grid()
    plt.show()

    x = np.linspace(1, 1000, 1000)

    dado1 = np.random.randint(1, 7, 1000)
    dado2 = np.random.randint(1, 7, 1000)

    tot = dado1 + dado2

    plt.subplots(figsize=(8, 4), dpi=100)

    plt.scatter(x, tot, color="green")
    plt.xlabel('lanci')
    plt.ylabel('somme')
    plt.show()

