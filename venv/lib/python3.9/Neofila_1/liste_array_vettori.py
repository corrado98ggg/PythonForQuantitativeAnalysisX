'''
possiamo utilizzare delle liste, un modo differente di chiamare gli array o i vettori.
I singoli elementi della lista (numeri, stringhe o qualsiasi altro tipo consentito)
sono compresi tra due parentesi quadre.
Per esempio, immaginiamo di definire una lista di ticker di titoli azionari americani:
'''



if __name__ == '__main__':
    titoli = ["AAPL", "AMZN", "BA", "GOOG", "IBM", "MSFT", "NFLX"]
    #in questo ambito è importante vedere che in python possimao stampare facendo lo sclicing
    print(titoli[1:4])
    print(titoli[-4:-1])
    print(titoli[0:8:2])
    print(titoli[0::2])
    print(titoli[::-1])

    #notare inoltre che abbiamo accesso a numeri metodi che ci permettono di effettuare delle operazioni sulla lista
    titoli.reverse()
    for titolo in titoli:          #il for è scritto in maniera differente dal c
        print(titolo);

    lista_numerica = []
    for x in range(1,11):
        lista_numerica.append(x)
    print(lista_numerica)

    #lo stesso costrutto lo possiamo fare usando la seguente nozione compatta:
    lista_numerica_1 = [x**2 for x in range(11)] #x**2 alla seconda
    print(lista_numerica_1)