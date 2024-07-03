import os
import time
import csv
os.system("cls")
from prueba3funciones import *

comuna = ("Santiago", "Colina", "Pirque")
valorcilindro5kg = 12500
valorcilindro15kg = 25500

listacliente = []



while True:
    os.system("cls")
    print("Bienvenido a la aplicacón de Gaxplosive")
    print("----------------------------------------")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")

    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("Ingrese una opción correcta")
        except:
            print("Ingrese un número entero")

    if opc == 1:
        registrar_cliente()

        

        pass

    elif opc == 2:
        listar_clientes()


    elif opc == 3:
        buscarpor_rut()
                


    elif opc == 4:
        importar_csv()

    else:
        print("Muchas gracias por ocupar la aplicación!")
        break
