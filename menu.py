from pprint import pprint
import inquirer
from central import *

'''
This class is used to create the menu for the user to interact with.
'''
class Menu():

    def __init__(self, _central):
        self.central = _central

    # -------- Llamadas ---------
    def llamar(self):
        self.showNumbers()

    def call(self):
        print("""
        1. Seleccionar un número telefónico
        2. Ingresar un número

        """)

        option = input("Seleccione una opción: ")
        if option == "1":
            self.show_numbers()
        elif option == "2":
            print("Seleccionó la opción 2")

    def show_numbers(self):
        questions = [
            inquirer.List(
                "Abonado",
                message="Elige el abonado al que desea llamar?",
                choices=self.central.get_abonados(),
            ),
        ]

        answers = inquirer.prompt(questions)
        self.make_call(answers['Abonado'].telefono)

    def make_call(self, number):
        print("Llamando a {}".format(number))
        
        # Check if the number is valid
        if not self.central.check_number(number):
            print("El número {} no existe".format(number))
            return

        # Show the number's information
        abonado = self.central.get_abonado(number)

        if (abonado.status == 0):
            print("El número {} está ocupado ".format(number))
            return
        elif (abonado.status == 1):
            self.setSoundCalling()
            print("El número {} está disponible".format(number))
            return
        else:
            print("El número {} está desactivado".format(number))
            return

    def setSoundCalling(self):
        print("Ring Ring")
        # TODO: Implementar el sonido de llamada


    def show_history(self):
        print("""
        1. Ver historial de llamadas
        2. Ver historial de llamadas de un número

        """)

        option = input("Seleccione una opción: ")
        if option == "1":
            print("Seleccionó la opción 1")
        elif option == "2":
            print("Seleccionó la opción 2")

    def show_billing(self):
        print("""
        1. Ver facturas
        2. Ver facturas de un número

        """)

        option = input("Seleccione una opción: ")
        if option == "1":
            print("Seleccionó la opción 1")
        elif option == "2":
            print("Seleccionó la opción 2")

        