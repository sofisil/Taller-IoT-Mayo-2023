import time

while True:
    temperatura = int(input('cual es la temperatura actual'))
    try:
        if 25>= temperatura >10:
            print(f'esta es la temperatura {temperatura}')
        else:
            print('no es una temperatura ideal')
        time.sleep(6)
    except KeyboardInterrupt:
        break

    