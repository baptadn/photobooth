import evdev
import time

device = evdev.InputDevice('/dev/input/event0')
print(device)
has_print = False

while True:
    event = device.read_one()
    if event and has_print == False and event.type == evdev.ecodes.EV_KEY and  event.value == 0:
        print("print")
        time.sleep(2)
        has_print = True
    elif event and event.type == evdev.ecodes.EV_KEY and event.value == 0:
         pass
    elif not event:
        has_print = False
