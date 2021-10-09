import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def import_file(filename):
    data = pd.read_csv(filename, parse_dates = ["Date"])
    data.set_index("Date", inplace = True)
    data.drop(["Time","OI"], axis = 1, inplace = True)
    return data

if __name__ == '__main__':
    FILENAME = "/Users/corrado/PycharmProjects/PythonForQuantitativeAnalysisX/venv/lib/python3.9/caricamento_dati_&_prime_elab/SPY_Daily.txt"
    data = import_file(FILENAME)
    print(data.tail(8))
    data.Close.plot()
    #personalizziamo il grafico che produciamo delle chiusure e notiamo le differenze
    plt.figure(figsize=(8, 4), dpi=100)
    plt.plot(data.Close, color='green')
    plt.xlabel("Tempo")
    plt.ylabel("Prezzi")
    plt.title("Chiusure - SPY daily")
    plt.grid(True)
    plt.show()
    #possiamo pure mettere due grafici vicini per confrontare meglio il da farsi

    fig, axes = plt.subplots(1, 2, figsize=(8, 4), dpi=100)
    axes[0].hist(data.Close, 100, orientation='horizontal', color='b', alpha=0.7)
    axes[0].set_title("Distribuzione Prezzi")
    axes[0].grid(True)
    axes[1].plot(data.Close, color='green')
    axes[1].set_title("Prezzi")
    axes[1].grid(True)
    plt.tight_layout()
    plt.show()