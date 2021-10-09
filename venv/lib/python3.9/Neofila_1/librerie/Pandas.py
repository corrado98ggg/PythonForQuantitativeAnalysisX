import pandas as pd
import numpy as np

'''si occupa di rendere efficiente la gestione di strutture dati anche di grandi dimensioni.
Ha due classi di oggetti che caratterizzano la libreria: le Series e i DataFrame. '''

if __name__ == '__main__':
    #Le Series di Pandas sono degli array di dati disposti su singola colonna.
    serie1 = pd.Series([1,2,3,4], name = "serie_prova")
    print(serie1)

    serie2 = pd.Series([1,2,3,4], index= {"A", "B", "c", "D"}, name="serie di prova")
    print(serie2)

    #DataFrame Pandas non è altro che un insieme di più Series combinate in una matrice di righe e colonne

    df = pd.DataFrame([np.random.randint(1,100,5) for x in range(5)], columns={"A", "B", "c", "D", "E"})
    print(df)
    print(df["A"])
    print(df.iloc[:,1])
    print(df.iloc[2:, 3:])
    print(df.loc[2])
    print(df > 50)
    df1 = df[df > 50]
    print(df1)
