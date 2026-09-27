# Specifico per leggere file in formato CSV
from csv import reader

# Apro un file ed ottengo un oggetto ad hoc per operare su di esso
filein = open("input.txt", "r")

#stringa = filein.read(10) # Posso leggere un certo numero di caratteri, es. 10
#print(stringa)

# Lettura e stampa nella console di un file un carattere alla volta con un ciclo while, fino a quando non trovo il terminatore ""
c = stringa = filein.read(1)
while c != "" :
    print(c, end="")
    c = stringa = filein.read(1)

filein.close() # Devo ricordarmi di chiudere il file

print("_________________")

filein = open("input.txt", "r") # Per leggere di nuovo devo riaprirlo
riga = filein.readline() # Posso leggere una riga alla volta
print(riga)
filein.close()

# Lettura e stampa nella console di un file riga per riga con for in

filein = open("input.txt", "r")
for riga in filein:
    print(riga, end="")
filein.close()

# Se volessi leggere tutto il file in un colpo solo?

#contents = filein.read()

# Ci sono poi file in formati particolari, esempio CSV

fileincsv = open("input_csv.txt", "r")

# Potrei leggerli come fatto sopra, oppure utilizzare un meccanismo particolare, basato sul reader

csv_reader = reader(fileincsv)

for row in csv_reader : # Posso leggere una riga alla volta ed ottenerne direttamente i campi che la compongono
    # print(row)
    campo1 = row[0]
    campo2 = row[1]
    campo3 = row[2]
    print(campo1+"; "+campo2+";"+campo3)