from pynput.mouse import Button, Controller
import time

mouse = Controller()

while True:
    # Obtener la posición actual del ratón
    mouse_pos = mouse.position
    print(f"Mouse en: ({mouse_pos[0]}, {mouse_pos[1]})")
    time.sleep(1)
