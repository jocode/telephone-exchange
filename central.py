from abonado import Abonado
import names
import random_number
from random import randint

MAX_ABONADOS = 20

# This class contains the functionality for the Telephone exchange
class CentralTelefonica():

    lista_abonados = []
    COST_PER_SECOND = 3.15 # Pesos colombianos

    def __init__(self, database):
        self.database = database
        self.lista_abonados = database.get_abonados()
        self.setup_abonados()
        self.setup_fuera_servicio()
        self.setup_ocupados()

    def setup_abonados(self):
        print(len(self.lista_abonados))
        if len(self.lista_abonados) > 0: 
            # Reset status to 1 for all abonados
            for i in range(0, len(self.lista_abonados)):
                self.lista_abonados[i].status = 1
            return

        # Create a list of abonados, if it is empty
        for i in range(0, MAX_ABONADOS):

            name = names.get_first_name()
            last_name = names.get_last_name()
            email = (name+last_name+"@gmail.com").lower()

            abonado = Abonado(
                name,
                last_name,
                random_number.get_random_number(),
                email
            )
            self.lista_abonados.append(abonado)
        
        # Save abonados to database
        self.database.save(self.lista_abonados)

            
    def setup_fuera_servicio(self):
        # Seleccionar aleatoriamente los abonados fuera de servicio
        for i in range(0, int(MAX_ABONADOS*0.15)):
            random = randint(0, len(self.lista_abonados)-1)

            while self.lista_abonados[random].status != 1:
                random = randint(0, len(self.lista_abonados)-1)

            # Se estable como fuera de servicio
            self.lista_abonados[random].status = 2

    def setup_ocupados(self):
        # Seleccionar aleatoriamente los abonados ocupados
        for i in range(0, int(MAX_ABONADOS*0.25)):
            random = randint(0, len(self.lista_abonados)-1)

            while self.lista_abonados[random].status != 1:
                random = randint(0, len(self.lista_abonados)-1)

            self.lista_abonados[random].status = 0  # Se estable como ocupado

    def get_abonados(self):
        return self.lista_abonados

    def get_ocupados(self):
        return [ocupado for ocupado in self.lista_abonados if ocupado.status == 0]

    def get_disponibles(self):
        return [disponible for disponible in self.lista_abonados if disponible.status == 1]

    def get_fuera_servicio(self):
        return [suspendido for suspendido in self.lista_abonados if suspendido.status == 2]


    def check_number(self, telefono):
        for abonado in self.lista_abonados:
            if abonado.telefono == telefono:
                return True
        return False

    def get_abonado(self, telefono):
        for abonado in self.lista_abonados:
            if abonado.telefono == telefono:
                return abonado
        return None


    def save_call(self, abonado, llamada):
        index = self.lista_abonados.index(abonado)
        self.lista_abonados[index].save_call(llamada)
        print(f"Guardando llamada en {index}... {self.lista_abonados[index]}")

        # for abonado in self.lista_abonados:
        #     print("{} llamadas de {}".format(len(abonado.lista_llamadas), abonado.telefono))

        self.database.save(self.lista_abonados) # Save to database


    def llamar(self):
        print("Llamando...")

    def ver_historial(self):
        print("Ver historial de llamadas...")

    def ver_facturacion(self):
        print("Ver facturacion...")
