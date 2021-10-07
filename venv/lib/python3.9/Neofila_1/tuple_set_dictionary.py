if __name__ == '__main__':

    '''Una tupla (in inglese tuple) è una sequenza IMMUTABILE di elementi: 
     possiedono una computazione più veloce e a una minore occupazione di memoria'''

    giorni_settimana = ("lunedì", "martedì", "mercoledì", "giovedì",
                        "venerdì", "sabato", "domenica")

    operatori = ("trader",)

    #data delle liste possiamo:
    chiusure = [11.21,11.31]
    volumi = [11232, 11234]

    coppie = list(zip(chiusure, volumi))
    print(coppie)


    '''Un set rappresenta invece un insieme aritmetico di elementi. Si tratta di un insieme mutabile, non ordinato.
    Ciò si declina nel fatto che non potremo fare riferimento a un indice progressivo.
    Non trattandosi di strutture ordinate, l’output in fase di stampa può non corrispondere a quello in fase di definizione. Il mancato ordinamento
    ha il vantaggio di consentire un accesso agli elementi ancora più rapido.'''

    insieme = {"alpha", "beta", "gamma", "delta"}

    '''Un dizionario (in inglese dictionary) è una struttura dati che permette di legare delle chiavi a dei valori.
    Ovviamente i valori possono essere una qualsiasi struttura dati Python (quindi non solo numeri, ma anche stringhe, liste e così via):'''

    dizionario = {"strumento": "AAPL", "Operazioni ": 124}
    print(len(dizionario))
    print(dizionario["strumento"])

    '''è possibi8le iterare con un ciclo ttte le coppie contenute in un dizionario
    mediante il metodo items()'''

    for key, value in dizionario.items():
        print(chiave + ": " + str(valore))
