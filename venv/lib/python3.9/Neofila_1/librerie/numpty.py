import numpy as np

'''È la libreria dedicata al calcolo algebrico più completa e rapida in assoluto.
Creata per la gestione di array e matrici, consente operazioni a velocità C.'''

if __name__ == '__main__':
    lista = [1, 2, 3]
    lista = np.array(lista)
    # più rapido e veloce di lista
    print(np.zeros(10))
    print(np.ones(4))
    print(np.repeat(5, 4))
    print(np.arange(10))
    print(np.random.randint(4,10,6))
    #matrici con numpty
    matrice = np.array([[1,2,3,4],[5,6,7,8]])
    print(matrice)
    #Una volta creata una matrice (o un array), è possibile applicare delle operazioni simultanee su tutti gli elementi
    #Tale metodo è detto broadcast.
    print(matrice / 2)
    print(matrice**2)
    matrice2 = np.random.random([5,5])
    print(matrice2)
    print(np.sum(matrice, axis=1)) #genererà la somma di tutti gli elementi riga per riga (sommando gli elementi per tutte le colonne).
    print(np.sum(matrice, axis=0)) #genererà la somma di tutti gli elementi colonna per colonna (sommando gli elementi per tutte le righe).
    #np.reshape(matrice, (8, 8)) #riprogettare lo spazio della matrice
    #possiamo creare una query su una matrice
    print(np.where(matrice2 > 1, 1, matrice2)) #condizone, se_vero, se_falso