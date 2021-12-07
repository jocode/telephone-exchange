from os import system
from central import *
from database import Database
from menu import Menu
"""
Implementar en python una Central Telefónica que cumpla con los siguientes requisitos:
- Debe tener una capacidad de 20 abonados (Usuarios)
- Al iniciar el programa, deben estar
    - 15% Abonados fuera de servicio
    - 25% Abonados ocupados
    - Los restantes 60% Abonados disponibles
- El usuario puede seleccionar cualquier abonado para llamar
- Cada digito numérico ingresado por el teclado, debe tener asociado un sonido
- Se deben generar tonos de señalización
    - Tono ocupado
    - Tono de llamada entrante
    - Mensaje de fuera de servicio
- Cuando se establezca la llamada, debe activarse una conversación, la cual debe ser reproducida y registrarse la duración de la llamada, para luego poder calcular el costo de la llamada
- Para ver la factura de un usuario, deben habersen realizado como mínimo dos llamadas

mdbo@yahoo.com
"""

def show_menu():
    print("""
    ........................................
    Bienvenido a la Central Telefónica.

    1. Hacer una llamada
    2. Ver historial de llamadas
    3. Ver facturas
    0. Salir
    ........................................
    """)


def setup_central():
    global lista_abonados, central
    database = Database('database.json')
    central = CentralTelefonica(database)
    lista_abonados = central.get_abonados()

    print(f"Inicializando Central Telefónica ({len(lista_abonados)} abonados) ...")
    print(f"Abonados fuera de servicio: {len(central.get_fuera_servicio())}")
    print(f"Abonados ocupados: {len(central.get_ocupados())}\n")

if __name__ == "__main__":
    setup_central()
    show_menu()
    menu = Menu(central)
    
    opcion = input("Ingrese una opción: ")
    print('\n')
    while opcion != "0":
        if opcion == "1":
            menu.call()
        elif opcion == "2":
            menu.show_history()
            system('pause')
        elif opcion == "3":
            menu.show_billing()
            system('pause')
        else:
            print("Opción inválida")
        
        show_menu()
        opcion = input("Ingrese una opción: ")
        print('\n')

    print("Gracias por usar la Central Telefónica")
    print("Hasta luego.\n")

