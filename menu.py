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
    def call(self):
        origen = self.select_phone("Elige el abonado desde el que desea llamar?", status=1)
        numero_destino = self.enter_number()
        
        while (numero_destino == origen.telefono):
            print("No puedes llamar al mismo número. \n")
            numero_destino = self.enter_number()

        self.make_call(origen, numero_destino)

    # Show the numbers availables on the central
    def select_phone(self, message = "Seleccione un número: ", status = -1):

        abonados = []
        if (status == -1):
            abonados = self.central.get_abonados()
        elif (status == 0):
            abonados = self.central.get_ocupados()
        elif (status == 1):
            abonados = self.central.get_disponibles()
        elif (status == 2):
            abonados = self.central.get_fuera_servicio()

        questions = [
            inquirer.List(
                "origen",
                message=message,
                choices=abonados,
            ),
        ]

        answers = inquirer.prompt(questions)
        return answers["origen"]
        

    def enter_number(self):
        self.show_abonados()
        print("Ingrese el número telefónico al que deseas llamar: ")
        key_logger() # 
        numero = input("\nNúmero ingresado: ")
        os.system('pause')
        return numero

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

    def make_call(self, origen, destino):
        print("\n")
        # Check if the number is valid
        if not self.central.check_number(destino):
            print("El número {} no existe".format(destino))
            os.system('pause')
            return

        # Show the number's information
        abonado = self.central.get_abonado(destino)

        if (abonado.status == 0):
            print("El número {} está ocupado ".format(destino))
            sound = pyglet.resource.media('sounds/busy_tone_effect.wav')
        elif (abonado.status == 1):
            print("Llamando de {} a {}".format(origen, destino))
            self.handle_calling(origen, destino)
            return
        else:
            print("El número {} está desactivado".format(destino))
            sound = pyglet.resource.media('sounds/phone_dead_line_effect.mp3')
            
        self.player.next_source()
        self.player.queue(sound)
        self.player.play()
        input('Presione una tecla para terminar la llamada. \n')
        self.player.pause()

    def handle_calling(self, origen, destino):
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
        conversation_cost = round(duration * self.central.COST_PER_SECOND, 2)
        llamada = Llamada(local_time, duration, conversation_cost, destino)
        self.central.save_call(origen, llamada)
        os.system('pause')


    # -------------- Show history of calls --------------
    def show_history(self):

        abonado = self.select_phone("Selecciona un número para ver su historial de llamadas. ")
        
        print(f"""
        -------------------------------------------------
            Historial de llamadas de {abonado.nombre} {abonado.apellido}
        -------------------------------------------------
                Fecha      Duración     Costo
        """)

        for llamada in abonado.get_history():
            print("\t* {0}".format(llamada))
        
        print("\n")

    def show_billing(self):
        
        abonado = self.select_phone("Selecciona un número para ver su factura. ")

        if (abonado.count_calls() < 2):
            print(f"\n Debes llamar al menos 2 veces para poder ver la factura de {abonado.telefono}.\n")
            return

        print(f"""
        -------------------------------------------------------------------------
        |              Factura de {abonado.nombre} {abonado.apellido} [{abonado.telefono}]                    |
        -------------------------------------------------------------------------
        |  Número    |           Fecha            | Duración   |    Costo       |
        """)

        for llamada in abonado.get_history():
            print("\t| {0} |\t {1} |\t {2} seg |\t ${3} |".format(abonado.telefono, llamada.fecha, llamada.duracion, llamada.costo))
        
        print("\n\t\t\t\t Total: ${} pesos".format(abonado.get_billing()))
        print("\t-------------------------------------------------------------------------")

        