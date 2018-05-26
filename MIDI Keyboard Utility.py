import pygame.midi

def main():
    pygame.midi.init()

    global devices
    devices = []

    for x in range(0, pygame.midi.get_count()):
        p = pygame.midi.get_device_info(x)
        devices.append(p)

    showDevicesType()

    c = input('\nSelect a device: ')

    try:
        c = int(c)
        inp = pygame.midi.Input(c)
    except:
        input('No match. Press return to quit...')
        exit(0)

    try:
        while True:
            if inp.poll():
                touch = inp.read(1000)
                if touch[0][0][2] != 0:
                    status = 'KEYDOWN'
                    print(str(touch[0][0][1] - 20), status)
                else:
                    status = 'KEYUP'
                    print(str(touch[0][0][1] - 20), status)
    except KeyboardInterrupt:
        pass

def showDevicesType():
    i = 0
    print('\nDetected devices: ')
    for item in devices:
        if item[2] == 1:
            dType = ' [Input]'
            print(str('{}. '.format(i)) + str(item[1] + dType))
            i += 1
        if item[3] == 1:
            dType = ' [Output]'
            print(str('{}. '.format(i)) + str(item[1] + dType))
            i += 1

if __name__ == '__main__':
    main()
