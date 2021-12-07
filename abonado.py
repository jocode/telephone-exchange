import json

class Abonado():

    STATUS = {
        0: 'Ocupado',
        1: 'Disponible',
        2: 'Fuera de servicio'
    }

    # Se crea el constructor de la clase, por defecto de crea un abonado como disponible
    def __init__(self, nombre, apellido, telefono, correo, saldo = 0, lista_llamadas = [], status = 1):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.saldo = saldo
        self.lista_llamadas = lista_llamadas # Diccionario
        self.status = status  # 0 = ocupado, 1 = disponible, 2 = suspendido

    def show_info(self):
        return '[{}] {} {} {}'.format(self.get_status(), self.nombre, self.apellido, self.telefono)

    # Setup status from user where 0 = ocupado, 1 = disponible, 2 = suspendido
    def set_status(self, status):
        self.status = status

    # Get status from user where 0 = ocupado, 1 = disponible, 2 = suspendido
    def get_status(self):
        return self.STATUS[self.status]

    def get_history(self):
        return [Llamada(**llamada) for llamada in self.lista_llamadas]

    def save_call(self, llamada):
        self.lista_llamadas.append(llamada.__dict__)

    def get_billing(self):
        # Suma el costo de las llamadas
        return sum([llamada['costo'] for llamada in self.lista_llamadas])

    def count_calls(self):
        return len(self.lista_llamadas)

    def __str__(self):
        return '[{}] {} {} {}'.format(self.get_status(), self.nombre, self.apellido, self.telefono)


class Llamada():

    def __init__(self, fecha, duracion, costo, numero_destino):
        self.duracion = duracion
        self.costo = costo
        self.numero_destino = numero_destino
        self.fecha = fecha

    def __str__(self):
        return '{}.   {} segundos.   ${} pesos'.format(self.fecha, self.duracion, self.costo)


    