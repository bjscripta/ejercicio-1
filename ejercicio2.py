import csv

persona= ["nombre","apellido"]
    
for i in range (3):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    persona.append(nombre)
    persona.append(apellido)

with open ("nombres_y_apellido.csv", "w",newline="") as archivo:
    escribir = csv.writer(archivo)
    escribir.writerows(persona)


