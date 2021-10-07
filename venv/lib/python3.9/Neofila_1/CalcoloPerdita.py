#codice per calcolare il profitto o la perdita di un'operazione finanziaria

"""
calcolo del profitto di un’operazione
di compravendita sul titolo
Boeing (ticker BA).

definiamo la direzione del trade tramite codice:
* stringa “LONG” per operazioni al rialzo
* “SHORT” per operazioni di short selling
"""


if __name__ == '__main__':
    ticket_strumento = str(input("inserire ticker strumento: "))
    direzione_trade = input("Inserire direzione del trade [LONG-SHORT]: ")

    prezzo_ingresso = float(input("inserire prezzo di igressso in posizone (aperto): "))
    prezzo_uscita = float(input("inserire prezzo di uscita dalla posizione (chiuso): "))
    numero_azioni = float(input("inserire numero azioni (unità): "))
    profitto = 0

    if direzione_trade == "LONG" or direzione_trade == "long":
        profitto = round(numero_azioni * (prezzo_uscita - prezzo_ingresso), 2)
    else:
        if direzione_trade == "SHORT" or direzione_trade == "short":
            profitto = -round(numero_azioni * (prezzo_uscita - prezzo_ingresso), 2)

print("")
print("Profitto operazione su titolo " + ticket_strumento + ": " + str(profitto) + " $")
