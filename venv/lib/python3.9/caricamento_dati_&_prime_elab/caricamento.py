import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv("/Users/corrado/PycharmProjects/PythonForQuantitativeAnalysisX/venv/lib/python3.9/caricamento_dati_&_prime_elab/SPY_Daily.txt", parse_dates=["Date"])
    data.set_index("Date", inplace=True) #Ora la colonna Date è popolata da Timestamps (e non più da stringhe), Come abbiamo già visto, l’attributo inplace = True permette di sostituire il DataFrame di partenza
    data.drop(["Time", "OI"], axis=1, inplace=True) #Per eliminare tali campi sfruttiamo il metodo drop
    print(data.tail())