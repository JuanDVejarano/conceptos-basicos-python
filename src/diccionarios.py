# declaracion de diccionarios
dic1 = dict()
dic2 = {}

# valores de diccionarios
print("diccionarios vacios")
print(dic1, dic2)

# type de diccionarios
print("type de diccionarios")
print(type(dic1), type(dic2))

# asignación de valores a los diccionarios
dic1 = dict({'nombre': 'Juan', 'edad': 25, 'altura': 1.75, 'es_estudiante': True})
dic2 = {'nombre': 'david', 'edad': 35, 'altura': 1.50, 'es_estudiante': False}

print("diccionarios con elementos")
print(dic1, dic2)

# impresion del valor en una posición del diccionario
print("valores de los diccionarios en la posición 'nombre'")
print(dic1['nombre'], dic2['nombre'])

# imprimir las llaves de un diccionario
print("imprimir las llaves de un diccionario")
print(dic1.keys(), dic2.keys())

# imporimir los valores de un diccionario y llaves por medio de un ciclo for
print("imporimir los valores de un diccionario y llaves por medio de un ciclo for")
for i, j in dic1.items():
    print(i, j)