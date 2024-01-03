import pyautogui
from pynput.mouse import Listener, Button


def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        current_x, current_y = pyautogui.position()
        print(f"Left button clicked at ({x}, {y}). Current position: ({current_x}, {current_y})")


with Listener(on_click=on_click) as listener:
    listener.join()
