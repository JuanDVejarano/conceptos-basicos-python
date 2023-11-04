
# Creamos un diccionario vacío
estudiantes = {}

# Agregamos estudiantes y sus notas
#estudiantes["Juan"] = [90, 85, 95]
#estudiantes["Maria"] = [80, 75, 70]
#estudiantes["Pedro"] = [95, 90, 92]

cantidad = int(input("Ingrese la cantidad de estudiantes a agregar: "))
for i in range(cantidad):
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []
    while nombre in estudiantes:
        print("El estudiante ya existe")
        nombre = input("Ingrese el nombre del estudiante: ")

    nota = 0
    print("Ingrese las notas del estudiante, para terminar ingrese un número negativo")
    while nota >= 0:
        nota = int(input("Ingrese la nota: "))
        if nota >= 0:
            notas.append(nota)
    estudiantes[nombre] = notas

for i, j in estudiantes.items():
    print("Estudiante: ", i, " Notas definitivas: ", sum(j)/len(j))

