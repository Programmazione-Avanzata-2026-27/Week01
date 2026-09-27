x = 5

y = x # Con questa istruzione nella variabile x finisce il contenuto di x

x = 3

print(x)
print(y) # Se stampo x o y, in entrambe ci sarà lo stesso valore

# Cosa succede invece con le liste, invece?

# Definisco una lista, il cui nome è scores
scores = [10, 9, 7 , 4]

# Scrivendo invece
values = scores # Ho definito un'altra lista, ma senza creare una nuova struttura dati in memoria

# Semplicemente, la variabile values fa riferimento all'area di memoria di scores (e dati in essa contenuti)

# Creo ora un'altra lista ancora
points = [1, 3, 5]

values = points # La variabile values ora fa riferimento a questa nuova lista, come points

scores = points # Anche scores

# Non c'è più modo di raggiungere la struttura dato che conteneva [10, 9, 7 , 4]