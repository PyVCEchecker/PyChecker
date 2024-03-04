import time
from alarmdecoder import AlarmDecoder
from alarmdecoder.devices import SocketDevice

# Configuration values
HOSTNAME = '10.1.10.26'
PORT = 10001

def main():
    """
    Example application that opens a device that has been exposed to the network
    with ser2sock or similar serial-to-IP software.
    """
    try:
        # Retrieve an AD2 device that has been exposed with ser2sock on localhost:10000.
        device = AlarmDecoder(SocketDevice(interface=(HOSTNAME, PORT)))

        # only needed for multi partition systems. Mask changes depending on keypad address partition assignment.
        #device._internal_address_mask = 0x800

        # Set up an event handler and open the device
        device.on_message += handle_message
        with device.open():
            while True:
                time.sleep(1)

                # Dump all the vars out for fun
                #from pprint import pprint
                #pprint(vars(device))

                # polling example testing object state after a message or at any time.
                # After every message we can test the new state.
                # Also we can setup handlers such as on_ready or on_??? for event driven code. 
                if (device._armed_status):
                    print ("armed away")
                elif (device._armed_stay):
                    print ("armed stay")
                else:
                    print ("disarmed",)
                    if (device._ready_status):
                       print ("ready to arm")
                    else:
                       print ("not ready")

    except Exception as ex:
        print('Exception:', ex)

def handle_message(sender, message):
    """
    Handles message events from the AlarmDecoder.
    """
    print(sender, message.raw)

if __name__ == '__main__':
    main()
