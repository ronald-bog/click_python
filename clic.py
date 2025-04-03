from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time

# Controlador del ratón
mouse = Controller()
keyboard = KeyboardController()

# Monitores (suponiendo un solo monitor para este ejemplo)
monitor1 = {
    'x': 0,
    'y': 0,
    'width': 1440,
    'height': 900,
}

# Coordenadas de clic
clickX = monitor1['x'] + 2584
clickY = monitor1['y'] + 297
clickX2 = monitor1['x'] + 2584
clickY2 = monitor1['y'] + 674
clickX3 = monitor1['x'] + 3295
clickY3 = monitor1['y'] + 178
clickX4 = monitor1['x'] + 3279
clickY4 = monitor1['y'] + 723
clickX5 = monitor1['x'] + 1204
clickY5 = monitor1['y'] + 294
clickX6 = monitor1['x'] + 1204
clickY6 = monitor1['y'] + 726
clickX7 = monitor1['x'] + 1863
clickY7 = monitor1['y'] + 303
clickX8 = monitor1['x'] + 1858
clickY8 = monitor1['y'] + 697

def auto_click():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    mouse.position = (clickX, clickY)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX}, {clickY}) en el monitor 1")


def auto_click2():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX2, clickY2)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX2}, {clickY2}) en el monitor 2")

def auto_click3():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX3, clickY3)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX3}, {clickY3}) en el monitor 3")

def auto_click4():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX4, clickY4)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX4}, {clickY4}) en el monitor 4")

def auto_click5():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX5, clickY5)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX5}, {clickY5}) en el monitor 5")

def auto_click6():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX6, clickY6)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX6}, {clickY6}) en el monitor 6")

def auto_click7():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX7, clickY7)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX7}, {clickY7}) en el monitor 7")

def auto_click8():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    # Mover el ratón y hacer clic izquierdo
    mouse.position = (clickX8, clickY8)
    mouse.click(Button.left)  # Usar Button.left en lugar de 'left'
    print(f"Clic izquierdo realizado en ({clickX8}, {clickY8}) en el monitor 8")


# Llamar a la función cada 9 segundos
while True:
    auto_click()
    auto_click2()
    auto_click3()
    auto_click4()
    auto_click5()
    auto_click6()
    auto_click7()
    auto_click8()
    time.sleep(9)


# (2563, 349)
# (2563, 710)
# (3279, 323)
# (3279, 723)
