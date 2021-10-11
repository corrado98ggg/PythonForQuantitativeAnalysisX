import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importa_file

'''La funzione SMA prende in argomento una serie e un periodo
e restituisce la media mobile corrispondente.
In questo modo sarà possibile calcolare una media mobile dei massimi (High),
oppure quella delle aperture (Open).'''

def SMA(array, period):
    """
    Funzione che calcola la media mobile semplice di una serie
    """
    return array.rolling(period).mean()

'''La funzione BollingerBand riceve invece tre parametri in argomento:
una serie, un periodo e un moltiplicatore.
Questo ci consente di generalizzare la funzione in modo da poter realizzare,
per esempio, delle bande a 3 o 4 deviazioni standard dalla media centrale.
Il segno del moltiplicatore decreterà se si tratti di una banda superiore o inferiore.'''

def BollingerBand(array,period,k):
    """
    Funzione che calcola una Banda di Bollinger di una serie
    """
    BB = SMA(array,period) + k * array.rolling(period).std()
    return BB

'''esempio di inserimento per il calcolo degli indici:
data['SMA200'] = SMA(data.Close,200)
data['BBU200'] = BollingerBand(data.Close,200,2)
data['BBL200'] = BollingerBand(data.Close,200,-2)
data.tail(10)'''

if __name__ == '__main__':
    FILENAME = "/Users/corrado/PycharmProjects/PythonForQuantitativeAnalysisX/venv/lib/python3.9/caricamento_dati_&_prime_elab/SPY_Daily.txt"
    data = importa_file.import_file(FILENAME)

    '''nuova colonna SMA200 (Simple Moving Average)
      e leggiamola da destra verso sinistra:
      applichiamo la funzione di media a una porzione
      a finestra scorrevole (rolling) di 200 record alla colonna delle chiusure.'''

    data["SMA200"] = data.Close.rolling(200).mean()
    print(data.tail())

    '''----> 
       L’indicatore cha viene è uno dei più utilizzati dai gestori di fondi per comprendere
       se un determinato strumento finanziario sia in trend rialzista o ribassista.
       Ciò può essere dedotto in base alla posizione reciproca tra chiusure e media mobile,
       oppure alla posizione reciproca tra due medie mobili di differenti periodi::

               • Close > SMA200: tendenza rialzista.
               • Close < SMA200: tendenza ribassista.

               • SMA50 > SMA200: tendenza rialzista.
               • SMA50 < SMA200: tendenza ribassista.    '''


    '''Bande di Bollinger:
    La banda superiore (BBU) sarà data dalla media mobile a 200 periodi,
    cui viene sommata la deviazione standard (funzione str()) calcolata su una finestra mobile di 200 periodi.
    La banda inferiore (BBL) sarà data invece dalla media mobile a 200 periodi,
    cui viene sottratta la stessa deviazione standard calcolata sulla finestra scorrevole di 200 periodi.'''

    #La codifica delle Bande di Bollinger, costruite intorno alla media mobile a 200 periodi.

    data["BBU200"] = data.SMA200 + 2 * data.Close.rolling(200).std()
    data["BBL200"] = data.SMA200 - 2 * data.Close.rolling(200).std()
    data.dropna(inplace=True)
    print(data.head(10))

    #Il grafico delle Bande di Bollinger costruite intorno alla media mobile a 200 periodi.
    plt.figure(figsize=(8, 4), dpi=100)
    plt.plot(data.SMA200, color='blue', linewidth=1.0)
    plt.plot(data.BBU200, color='lime', linewidth=1.0)
    plt.plot(data.BBL200, color='red', linewidth=1.0)
    plt.plot(data.Close, color='green', linewidth=1.0)
    plt.xlabel("Tempo")
    plt.ylabel("Prezzi")
    plt.title("Chiusure e Bollinger Bands - SPY daily")
    plt.grid(True)
    plt.show()