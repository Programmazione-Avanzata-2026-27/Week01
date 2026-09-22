# Spesso i programmi Python includono una funzione principale, convenzionalmente chiamata main()

def main():
    x = 5
    print(x)

    # Una variabile stringa, tipo di dato particolare in Python, si defnisce come altre, con =

    stringa = 'La "mia"\nstringa' # Il contenuto può essere tra ' ' o tra " " e posso avere sequenze di escape, es. \n per andare a capo

    # Per stampare una stringa nella console si può continuare ad usare print()

    print(stringa)

    # E' possibile usare l'operatore + per concatenare stringhe tra loro

    firstName = "Harry"
    lastName = "Morgan"
    name = firstName +" "+ lastName
    print("Il nome è: "+name)

    # E' anche possibile concatenare stringhe e valori numerici

    y = 6
    print("Il valore della variabile y è: " + str(y)) # Ma occorre prima convertire questi ultimi con la funzione str()

    # Per accedere ai caratteri di una stringa si usa nome_strina[indice], con indice a partire da 0 fino a len(nome_stringa)-1

    first = name[0]
    print(first)

    # In Python, le stringhe sono in effetti degli oggetti, elementi particolari che portano con sé alcune proprietà/funzionalità

    # Queste proprietà/funzionalità sono accessibili con il .

    maiuscola = stringa.upper() # Esempio, upper() è una funzione che converte il contenuto della stringa in maiuscolo, e restituisce il risultato

    # Maggiori informazioni, es. sulle funzioni di str qui: https://docs.python.org/3/builtins/stdtypes.html#string-methods

    print(maiuscola)

    # Per leggere dalla tastiera si può utilizzare la funzione input(), che restituisce una stringa

    # stringa_eta = input("Quanti anni hai? ")
    stringa_eta = 51
    print("Hai: "+stringa_eta)
    if int(stringa_eta)>30 :
        print("Boomer")

    # La funzione print() possiede parametri che consentono, es., di non andare a capo (end='')

    print("PRIMO", end=", ")
    print("SECONDO", end=", ")
    print("TERZO")

    # Python possiede istruzioni per controllare il flusso, es., per costrutti di selezione o scelta (if, ...)

    z = 20 # Variabile utilizzata nell'espressione che definisce la condizione
    if z == 20: # Il : apre un blocco, nel quale le istruzioni sono indentate/rientrate
        print("z è uguale a venti") # Ramo True
        # Altre istruzioni del blocco/ramo True
    else:
        print("z non è uguale a venti") # Ramo False
        # Altre istruzioni del blocco/ramo False

    # Python possiede poi istruzioni per la gestione delle iterazioni (cicli)

    # Ad esempio, il while, (principalmente/tipicamente) per cicli controllati da eventi

    counter = 1 # Inizializza la condizione
    while counter <= 10 : # Verifica la condizione
        print(counter)
        counter = counter + 1 # Aggiorna la condizione

    # Alternativa, il for, per cicli controllati da un contatore o, più in generale, basati su di un contenitore

    for i in range(1, 10): # In questo caso, il contenitore è quello creato dalla funzione range(), un contenitore di 10 interi in sequenza
        print(i)


# Invocando la funzione main(), che in questo caso contiene tutto il codice, si da avvio al programma
main()