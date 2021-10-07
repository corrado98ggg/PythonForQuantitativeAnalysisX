'''È infatti possibile scomporre
la realtà in oggetti elementari a
complessità crescente'''

class portafoglio():

    def __init__(self,denaro):
        self.denaro = denaro
        self.valuta = "EUR"

    def stampaconto(self):
        return "denaro presente: " + str(self.denaro) + " " + self.valuta


    def transazione(self, ammontatore):
        if ammontatore > 0 and abs(ammontatore) > self.denaro:
            print("Sul conto non ci sono abbastanza fondi per effetuare l'operazione")
        else:
            self.denaro += ammontatore
'''Nella riga 1 definiamo l’oggetto mediante la parola riservata class.
    Nella riga 3 vediamo invece quella che sembra la definizione di una funzione (in effetti si tratta proprio di una funzione),
    detta “costruttore” della classe __init__.
    Il termine è associato al fatto che determina la costruzione degli attributi della classe.
    Ogni volta che verrà creata un’istanza della classe Portafoglio, verrà invocato il metodo costruttore.
    Ma vediamo in dettaglio com’è fatto: vengono passati in argomento due elementi, self e denaro.
    Mentre il secondo banalmente rappresenta la quantità di denaro assegnata a quel particolare portafoglio, il primo può risultare piuttosto criptico.
    Si tratta di un riferimento a “sé stesso”,
    nel senso che quando viene creata l’istanza della classe (si pensi al gatto di classe animale),
    quel costruttore fa riferimento proprio a quell’istanza particolare. Per lo stesso motivo nella riga 4 si utilizza il prefisso self,
    per definire che l’attributo denaro della classe Portafoglio,
    cui viene associata la quantità di denaro passata in argomento,
    deve essere associata proprio a questa istanza.'''


if __name__ == '__main__':
    mio_portafoglio = portafoglio(1000)
    print(mio_portafoglio.denaro)
    print(mio_portafoglio.valuta) #Il nuovo attributo si chiama valuta e non è passato come argomento del costruttore, come avveniva per denaro: è una costante e in questo caso è associata alla stringa “EUR”
    print(mio_portafoglio.stampaconto())
    mio_portafoglio.transazione(2000)