from fsuipc import FSUIPC

with FSUIPC() as fsuipc:
    prepared_data = fsuipc.prepare_data([
        (0x0BC8, "h"), # offset set parking brake
        (0x7FFF, "h")  # offset release parking brake
    ], True)

    print("\nSet parking brake...")

    set_parkbrake, release_parkbreak = prepared_data.read()

    try:
        # when parking brake is off => turn on
        if set_parkbrake == int(0):
            prepared_data.write([0x0BC8, 0x7FFF])
            print('Parking brake: On...')

    except Exception as e:
        print('Error: Could not set the parking brake')

    input('Press any button to quit...')
