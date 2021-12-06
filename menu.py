from math import ceil, floor
from pprint import pprint
import random
import inquirer
from central import *
import pyglet
import time
import os
from abonado import Llamada
from keylogger import key_logger
from colorama import Fore, Back, Style  # https://www.geeksforgeeks.org/print-colors-python-terminal/


'''
This class is used to create the menu for the user to interact with.
'''
class Menu():

    def __init__(self, _central):
        self.player = pyglet.media.Player()
        self.conversations = ['conversation_1.wav', 'conversation_2.wav']
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
            self.enter_number()

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

    def enter_number(self):
        self.show_abonados()
        print("Ingrese el número telefónico: ")
        key_logger() # 
        numero = input("\nNúmero ingresado: ")
        os.system('pause')
        self.make_call(numero)

    # -------- Abonados ---------
    def show_abonados(self):
        for abonado in self.central.get_abonados():
            if (abonado.status == 2):
                print(Fore.RED, abonado.show_info())
            elif (abonado.status == 1):
                print(Fore.GREEN, abonado.show_info())
            else:
                print(Fore.CYAN,  abonado.show_info())

        print(Style.RESET_ALL)

    def make_call(self, number):
        print("\n")
        # Check if the number is valid
        if not self.central.check_number(number):
            print("El número {} no existe".format(number))
            os.system('pause')
            return

        # Show the number's information
        abonado = self.central.get_abonado(number)

        if (abonado.status == 0):
            print("El número {} está ocupado ".format(number))
            return
        elif (abonado.status == 1):
            print("Llamando a {} ...".format(number))
            self.handle_calling(abonado)
            return
        else:
            print("El número {} está desactivado".format(number))
            return

    def handle_calling(self, abonado):
        sound = pyglet.resource.media('sounds/phone_call_sound_effect.wav')
        self.player.next_source()
        self.player.queue(sound)
        self.player.play()
        wait = randint(3, floor(5)) # sound.duration
        time.sleep(wait)
        self.player.next_source()
        conversation = pyglet.resource.media('sounds/conversations/' + random.choice(self.conversations))
        self.player.queue(conversation)
        self.player.play()
        ti = time.time()
        input('Presione una tecla para terminar la llamada. \n')
        self.player.pause()
        
        tf = time.time()
        duration = ceil(tf - ti)
        local_time = time.ctime(ti)
        print('Duración de la llamada: {} segundos\n'.format(duration))
        # Save the call in the history
        llamada = Llamada(local_time, duration, 3, abonado.telefono)
        self.central.save_call(abonado, llamada)
        os.system('pause')



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

        