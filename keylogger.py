from pynput.keyboard import Key, Listener
from pyglet.resource import media

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def on_press(key):
    digito = str(key).replace("'", "")
    if digito in numbers:
        music = media(f'sounds/tones/t{digito}.wav')
        music.play()
        print(digito, end=" ", flush=True)
    elif key == Key.enter:
        return False
    else:
        print("\n[ERROR] Debes digitar un número")
        return False


def key_logger():
    with Listener(on_press=on_press) as listener:
        listener.join()


    
