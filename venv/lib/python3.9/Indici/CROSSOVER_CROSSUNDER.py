'''
stiamo interrogando la nostra serie di dati,
per comprendere dove si sia verificato un superamento del Donchian-ChannelUp da parte delle Close.
Dato che, a parità di record, la chiusura potrà al più essere uguale al massimo dei massimi, ma mai superiore,
faremo il confronto tra chiusure e Donchian della barra precedente.
Trattandosi di una relazione booleana
come prodotto otterremo appunto una serie booleana,
con True laddove la relazione si sia verificata
False in caso contrario.'''

def crossover(array1, array2):
    return (array1 > array2) & (array1.shift(1) < array2.shift(1))

def crossunder(array1, array2):
    return (array1 < array2) & (array1.shift(1) > array2.shift(1))

