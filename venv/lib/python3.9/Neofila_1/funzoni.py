def somma(numero, numero2):
    global ret   #posso dichiarare una variabile globale anche dentro una funzione
    ret = numero + numero2

def helloworld():
    print("helloworld!")

if __name__ == '__main__':
    helloworld()
    somma(3,5)
    print(ret)

    '''esiste una categoria particolare di funzioni anonime chiamate lambda. È possibile utilizzarle quando non si intende
    o non conviene definire una funzione classica.'''

    print((lambda x: x ** 2)(2))
    print((lambda x, y: x + y)(11, 22))
    print((lambda x: x if x % 2 == 0 else x ** 3)(3))