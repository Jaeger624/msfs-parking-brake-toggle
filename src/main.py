from fsuipc import FSUIPC

def set_parking_brake():
    print('Parking brake changed to: On')

def release_parking_brake():
    print('Parking brake changed to: Off')

with FSUIPC() as fsuipc:
    msfs = fsuipc.prepare_data([
        (0x0BC8, "l") # offset parking brake
    ], True)

    initial = True

    while True:
        parkbrake = msfs.read()

        if initial:
            if parkbrake[0] == int(229375):
                print('Current parking brake status: On\n')

            elif parkbrake[0] == int(0):
                print('Current parking brake status: Off\n')

            else:
                print('Current parking brake status: Unknown\n')

            initial = False

        else:
            if parkbrake[0] == int(229375):
                try:
                    print('Parking brake changed to: On')
                except:
                    print('Could not change status of parking brake')

            elif parkbrake[0] == int(0):
                try:
                    msfs.write('0x0BC8', 1)
                    print('Parking brake changed to: On')
                except Exception as e:
                    print(e)
                    print('Could not change status of parking brake')

            else:
                print('Parking brake changed to: Unknown')

        input("Press ENTER to toggle parking brake status!\n")


