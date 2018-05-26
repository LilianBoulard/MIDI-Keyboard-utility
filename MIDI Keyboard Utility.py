import pygame.midi, pyautogui
from dic import bindage

def main():
    pygame.midi.init()

    global devices
    devices = []

    for x in range(0, pygame.midi.get_count()): #Detects the MIDI devices conected
        p = pygame.midi.get_device_info(x)
        devices.append(p)

    showDevicesType()

    c = input('\nSelect a device: ') #For now, only input devices are supported

    try:
        c = int(c)
        inp = pygame.midi.Input(c)
    except:
        input('No match. Press return to quit...')
        exit(0)

    try:
        print('\nStream: \n\n')
        while True:
            if inp.poll():
                touch = inp.read(1) #Get the stream from the midi device
                if touch[0][0][2] != 0:
                    n = str(touch[0][0][1] - 20)
                    t = bindage["{}".format(n)]
                    if type(t) is list:
                        pyautogui.keyDown(bindage[n][0])
                        pyautogui.keyDown(bindage[n][1])
                        pyautogui.keyUp(bindage[n][1])
                        pyautogui.keyUp(bindage[n][0])
                    else:
                        pyautogui.keyDown(t)
                        pyautogui.keyUp(t)

    except KeyboardInterrupt:
        pass

def showDevicesType():
    i = 0
    print('\nDetected devices: ')
    for item in devices:
        if item[2] == 1:
            print(str('{}. '.format(i)) + str(item[1] + ' [Input]'))
        elif item[3] == 1:
            print(str('{}. '.format(i)) + str(item[1] + ' [Output]'))
        else:
            print(str('{}. '.format(i)) + str(item[1] + ' [No Type]'))
        i += 1

if __name__ == '__main__':
    main()
