# Come gestire gli errori (senza le eccezioni) ...

"""
stringa = input("Inserisci un numero intero: ")
print(stringa)
if stringa.isdigit():
    numero = int(stringa)
    risultato = numero/2
    print(f"Il risultato della divisione è {risultato}")
else:
    print("Ho detto un numero intero!!!")
"""

# ... e con le eccezioni ...

stringa = input("Inserisci un numero intero: ")
try:
    # Qui dentro metto le istruzioni che possono dare anomalie
    numero = int(stringa)
    risultato = numero/2
    print(f"Il risultato della divisione è {risultato}")
    # Se tutto va bene arrivo fino a qui
except ValueError:
    # Se per caso si scatena un'eccezione di tipo ValueError, finisco qui dentro
    print("Ho detto un numero intero!!!")
except TypeError: # Anche più di un blocco except, uno per possibile tipo di eccezione
    print("Altro tipo di errore")
finally:
    #Tutto il codice che voglio venga eseguito comunque alla fine
    pass

# Come scatenare un'eccezione intenzionalmente

raise ValueError("La mia eccezione di tipo ValueError")

