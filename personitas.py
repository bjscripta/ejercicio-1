import csv
personas = []
while True:
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = input("Ingrese edad: ")
    persona = [nombre,apellido,edad]
    personas.append(persona)
    opc = input("Desea agregar otra persona? (S/N)").lower()
    if opc=="no":
        break

with open("listado_personas.csv", "w",newline="") as archivo:
    write = csv.writer(archivo)
    write.writerows(personas)