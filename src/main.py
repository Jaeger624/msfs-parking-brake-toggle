from fsuipc import FSUIPC


with FSUIPC() as fsuipc:
    msfs = fsuipc.prepare_data([
        (0x0BC8, "l") # offset parking brake
    ], True)

    parkbrake = msfs.read()

    if parkbrake[0] == int(229375):
        print('Park-Brake: On')
    elif parkbrake[0] == int(0):
        print('Park-Brake: Off')
    else:
        print('Park-Brake: Unknown')