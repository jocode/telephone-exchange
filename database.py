import json
from abonado import Abonado
# Save file on json file
class Database:

    def __init__(self, fileName):
        self.db = []
        self.file_name = fileName
        self.loadFile()

    def loadFile(self):
        try:
            with open(self.file_name, 'r') as file:
                self.db = json.load(file)
        except:
            print("No se pudo cargar el archivo")

    # Save data on a JSON file
    def saveFile(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.db, file, indent=4)

    # Save file on json file. Receive a list of abonados
    def save(self, data):
        self.db = self.serialize(data)
        
        # for abonado in self.db:
        #     print("Llamadas realizadas: ", abonado['lista_llamadas'])

        self.saveFile()

    # Serialize data
    def serialize(self, data):
        return [abonado.__dict__ for abonado in data]

    def load(self):
        return self.db

    # Load data deserialized from JSON file
    def get_abonados(self):
        return [Abonado(**abonado) for abonado in self.db]