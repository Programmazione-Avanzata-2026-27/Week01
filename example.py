# Importazione del modulo math
import math
# Importazione della funzione sqrt dal modulo math
from math import sqrt

# Definizione di una variazione ed assegnazione del valore (intero) 10
bottles = 10

# In altri linguaggi, es., C, C++, Java, ... sarebbe stato necessario specificare il tipo di dato
# int bottles = 10;
# bottles = 4.5;

# E, in quegli altri linguaggi, il tipo non sarebbe potuto cambiare (se lo si fosse fatto, errore segnalato)

# In Python c'è più flessibilità, si può assegnare un valore di altro tipo alla medesima variabile

bottles = 'ten'

# Attenzione alle operazioni che però poi vengono effettuate: è compito del programmatore ricordare il tipo

# computation = bottles / 10 # Esempio, errre in questa divisione di una stringa per un numero

# Definizione di constanti (ma non c'è garanzia che il valore non possa essere cambiato dal programmatore)

BOTTLE_VOLUME = 0.75

# Alle variabili possono essere assegnati valori diversi, int, float, str, ... anche None

la_mia_variabile = 5.6

laMiaVariabile = 7.8

laMiaVariabile = None

#def la_mia_funzione(  ) :
    # Le varie istruzioni che intendo ripetere quana la funzione viene invocata
    # ...
    # ...

# Definizione di una funzione, eventualmente (come in questo caso), con parametri

def eleva_a_potenza( numero , esponente ):
    risultato = numero ** esponente
    return risultato # Istruzione utilizzata per restituire un valore

# Invocazione della funzione, con argomenti costanti (che vengono copiati nei parametri)

r = eleva_a_potenza(5, 12)

# Gli argomenti possono anche essere variabili, il cui valore viene copiato nei parametri all'atto della invocazione della funzione

n = 6
e = 8

# Il risultato della funzione restituito con return può essere memorizzato (in questo caso nella variabile r)

r = eleva_a_potenza(n, e)

# Per stampare nella console posso usare la funzione print(), che può stampare diversi contenuti

# Ad esempio ua variabile

print(r)

# Oppure una costante numerica

sqrt(56)

# Esistono anche funzioni di conversione

valore_con_virgola = 6.78
valore_intero = int(valore_con_virgola) # int() converte in un intero

print(valore_intero)

