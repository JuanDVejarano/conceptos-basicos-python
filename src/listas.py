# declaración de listas
lista1 = list()
lista2 = []

# impresión de listas
print("listas vacías")
print(lista1, lista2)

# impresión de tipos de listas
print("tipo de lista1 y lista2")
print(type(lista1), type(lista2))

# asignación de valores a las listas
lista1 = list([1, 2, 3, 4, 5])
lista2 = [5, 4, 3, 2, 1]

# impresión de listas con elementos
print("listas con elementos")
print(lista1, lista2)

# impresion del valor en una posición de la lista
print("valores de las listas en la posición 1")
print(lista1[1], lista2[1])

# agregar un elemento al final de la lista
print("agregar un elemento a la lista usando append")
lista1.append(6)
lista2.append("cero")
print(lista1, lista2)

# agregar un elemento en una posición específica
print("agregar un elemento en una posición específica usando insert")
lista1.insert(2, 'elemento especifico')
lista2.insert(2, 'elemento especifico')
print(lista1, lista2)

# modificar un elemento en una posición específica
print("modificar un elemento en una posición específica")
lista1[2] = 'elemento modificado'
lista2[2] = 'elemento modificado'
print(lista1, lista2)

# eliminar un elemento en una posición específica
print("eliminar un elemento en una posición específica usando del (posición 2)")
del lista1[2]
del lista2[2]
print(lista1, lista2)

# eliminar un elemento usando remove solo borra el primero que encuentra de izquierda a derecha
print("eliminar un elemento usando remove el (5)")
lista1.remove(5)
lista2.remove(5)
print(lista1, lista2)

# eliminar un elemento usando pop solo borra el ultimo elemento de la lista o el que se le indique por posición en su argumento
print("eliminar un elemento usando pop en la lista 1 el ultimo elemento y en la lista 2 el elemento en la posición 2")
lista1.pop()
lista2.pop(2)
print(lista1, lista2)

# unir dos listas
print("unir dos listas usando +")
lista3 = lista1 + lista2
print(lista3)

# repetir una lista
print("repetir una lista usando * iterandolo 3 veces")
lista4 = lista3 * 3
print(lista4)

# invertir una lista
print("invertir una lista usando reverse")
lista4.reverse()
print(lista4)

#lista con numeros desordenados
lista5 = [5, 2, 3, 1, 4]
print(lista5)

# ordenar una lista
print("ordenar una lista usando sort")
lista5.sort()
print(lista5)

# reversar una lista con ::-1
print("reversar una lista usando ::-1")
lista5 = lista5[::-1]
print(lista5)

# vaciar una lista
print("vaciar una lista usando clear")
lista5.clear()
print(lista5)
