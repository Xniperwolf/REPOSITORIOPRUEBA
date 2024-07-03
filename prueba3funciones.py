import os
import time
import csv

listacliente = []
comuna = ("Santiago", "Colina", "Pirque")
valorcilindro5kg = 12500
valorcilindro15kg = 25500


def registrar_cliente():
        os.system("cls")
        while True:
            try:
                rutcliente = int(input("Ingrese RUT cliente (sin guión ni puntos y reemplazar k por 0): "))
                if rutcliente.is_integer:
                    break
                else:
                    print("Ingrese RUT correcto de 9 dígitos")
            except:
                print("Ingrese numeros enteros")

        while True:
            nombrecliente = input("Ingrese Nombre de Cliente: ")
            if len(nombrecliente) >= 3 and nombrecliente.isalpha:
                break
            else:
                print("Nombre incorrecto, debe tener más de 3 caracteres y solo letras")

        while True:
            direccióncliente = input("Ingrese dirección de Cliente: ")
            if len(direccióncliente) > 3:
                break
            else:
                print("Ingrese una dirección correcta de más de 3 caracteres")

        while True:
            comunacliente = input("Ingrese comuna: ")
            if comunacliente in comuna:
                break
            else:
                print("Ingrese una comuna válida (Santiago, Colina, Pirque)")

        while True:
            try:
                cantcilindro5kg = int(input("Ingrese cantidad de cilindro de 5kg a llevar: "))
                if cantcilindro5kg >= 0:
                    break
                else:
                    print("ERROR! debe poner un número positivo mayor o igual a 0")
            except:
                print("ERROR, deben ser números enteros")

        while True:
            try:
                cantcilindro15kg = int(input("Ingrese cantidad de cilindros de 15kg a solicitar: "))
                if cantcilindro15kg >= 0:
                    break
                else:
                    print("ERROR! debe poner un número positivo mayor o igual a 0")
            except:
                print("ERROR! debe ser un número entero positivo")

        print("Cliente Registrado con éxito!")
        time.sleep(1)

        print("El valor del cilindro de 5kg es de 12500")
        time.sleep(2)
        print("El valor de un cilindro de 15kg es de 25500")
        print("--------------------------------------------")
        time.sleep(2)
        totalcompra = (valorcilindro15kg*cantcilindro5kg)+(valorcilindro15kg*cantcilindro15kg)
        print("Total de compra: ", totalcompra)
        time.sleep(2)

        diccionariocliente = {"RUT": rutcliente, "Nombre": nombrecliente, "Direccion": direccióncliente, "Comuna": comunacliente, "Cil5kg": cantcilindro5kg, "Cil15kg": cantcilindro15kg, "Total": totalcompra}
        listacliente.append(diccionariocliente)


def listar_clientes():
        os.system("cls")
        if len(listacliente) == 0:
            print("Lista vacía, elija opción 1")
        else:
            print("Clientes registrados")
            print("---------------------")
            for x in listacliente:
                print(f"RUT: {x['RUT']}\n Nombre: {x['Nombre']}\n Dirección: {x['Direccion']}\n Comuna: {x['Comuna']}\n Cil5kg: {x['Cil5kg']}\n Cil15kg: {x['Cil15kg']}\n Total: {x['Total']}\n")
                time.sleep(5)

def buscarpor_rut():
        os.system("cls")
        if len(listacliente) == 0:
            print("ERROR, RUT no encontrado")
        else:
            rutcliente = int(input("Ingrese RUT de cliente a buscar (Sin guión ni puntos, dígito k reemplazar por 0): "))
            if rutcliente in listacliente:
                for c in listacliente:
                    print("Cliente Encontrado")
                    print(f"Nombre: {c['Nombre']}\n Direccion: {c['Direccion']}\n Comuna: {c['Comuna']} Cil5kg: {c['Cil5kg']} Cil15kg: {c['Cil15kg']}\n Total: {c['Total']}\n")
                    time.sleep(3)


def importar_csv():
        hojaderuta = input("Ingrese ruta para crear archivo (Santiago, Colina, Pirque): ")
        if hojaderuta in comuna:
            with open ("Hojaderuta.csv","w", newline="") as archivo:
                encabezado = ["RUT","Nombre","Direccion","Comuna","Cil5kg","Cil15kg","Total"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(listacliente)


