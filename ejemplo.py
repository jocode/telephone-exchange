from pprint import pprint
import inquirer
from central import *

central = CentralTelefonica()

questions = [
    inquirer.List(
        "Abonado",
        message="Elige el abonado al que desea llamar?",
        choices=lista_abonados,
    ),
]

answers = inquirer.prompt(questions)
print(answers)