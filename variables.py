x = 5 # Globale, visibile ovunque ...

def funzione():
    # Variabile locale (alla funzione, al blocco)
    y = 6
    print(y)
    x = 3 # Questa x nasconde la variabile x globale
    print(x)
    # Se volessi utilizzare la variabile x globale nella funzione dovrei premettere la parola chiave global
    # global x

funzione()

# Se qui stampo x nella console vedrò 5, in quanto la variabile x locale alla funzione
# è stata usata e rimossa al termine dell'esecuzione della funzione

print(x)

# print(y) # Fuori dalla funzione la variabile y non esiste, questa istruzione segnala errore