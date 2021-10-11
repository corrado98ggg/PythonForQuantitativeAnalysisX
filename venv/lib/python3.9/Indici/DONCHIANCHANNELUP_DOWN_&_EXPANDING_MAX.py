import matplotlib.pyplot as plt
import CROSSOVER_CROSSUNDER
import importa_file

'''
NOZIONE TEORICA:

famiglia di sistemi di trading/investing che basano il loro funzionamento sull’assunto
che una tendenza impulsiva tenderà a continuare nel tempo.
Se si manifesta una tendenza, lo vedremo dalla dinamica dei prezzi
e proveremo a cavalcare tale indicazione direzionale. 
Stiamo parlando del principio dell’inerzia di mercato.

INTRODUCIAMO NUOVI INDICATORI:

ExpandingMax (che restituirà il massimo assoluto della serie punto per punto)
il DonchianChannelUp (che rappresenta il massimo dei massimi a finestra scorrevole)
il DonchianChannelDown (uguale al minimo dei minimi a finestra scorrevole).

'''


def ExpandingMax(array):
    """
    Funzione che calcola il massimo assoluto in avanzamento della serie
    """
    return array.expanding().max()

def DonchianChannelUp(array,period):
    """
    Funzione che calcola il massimo dei massimi di una serie
    a finestra scorrevole
    """
    return array.rolling(period).max()

def DonchianChannelDown(array,period):
    """
    Funzione che calcola il massimo dei massimi di una serie
    a finestra scorrevole
    """
    return array.rolling(period).min()

if __name__ == '__main__':
    FILENAME = "/Users/corrado/PycharmProjects/PythonForQuantitativeAnalysisX/venv/lib/python3.9/caricamento_dati_&_prime_elab/SPY_Daily.txt"
    data = importa_file.import_file(FILENAME)
    data["ExpMax"] = ExpandingMax(data.High)
    data["DonchianChannelUp"] = DonchianChannelUp(data.High, 50)
    data["DonchianChannelDown"] = DonchianChannelDown(data.Low, 50)
    print(data.tail())

    plt.figure(figsize=(8, 4), dpi=100)
    plt.plot(data.ExpMax, color='red', linewidth=1.0)
    plt.plot(data.Close, color='green', linewidth=1.0)

    plt.xlabel("Tempo")
    plt.ylabel("Prezzi")
    plt.title("Expanding Max - SPY daily")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 4), dpi=100)
    plt.plot(data.DonchianChannelUp, color='blue', linewidth=1.0)
    plt.plot(data.DonchianChannelDown, color='red', linewidth=1.0)
    plt.plot(data.Close, color='green', linewidth=1.0)
    plt.xlabel("Tempo")
    plt.ylabel("Prezzi")
    plt.title("Donchian Channel - SPY daily")
    plt.grid(True)
    plt.show()

    rule = CROSSOVER_CROSSUNDER.crossover(data.Close, data.DonchianChannelUp.shift(1))
    print(rule.tail(10))