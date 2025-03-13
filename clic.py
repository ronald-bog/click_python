from pynput.mouse import Controller, Button
import time

# Controlador del ratón
mouse = Controller()

# Monitores (suponiendo un solo monitor para este ejemplo)
monitor1 = {
    'x': 0,
    'y': 0,
    'width': 1440,
    'height': 900,
}

# Coordenadas de clic
clickX = monitor1['x'] + 3269
clickY = monitor1['y'] + 860


def auto_click():
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX, clickY)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX}, {clickY}) en el monitor 1")


# Llamar a la función cada 9 segundos
while True:
    auto_click()
    time.sleep(9)
