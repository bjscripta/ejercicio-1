import csv
from csv_con_python import * 

listnombre = []

with open ("nombres.csv", "w",newline="") as archivo:
    escribir = csv.writer(archivo)
    for j in range (3):
        nombre = input("Ingrese nombre: ")
        listnombre.append(nombre)
        escribir.writerow(listnombre)

def nombrelargo(p_lista):
    for i in range (3):
        if i==0:
            nombrelargo = p_lista[0]
        else:
            if len(p_lista[i]) > len(nombrelargo):
                nombrelargo = p_lista[i]
    print ("El nombre mas largo es ", nombrelargo)