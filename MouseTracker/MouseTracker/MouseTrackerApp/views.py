import pyautogui
from django.shortcuts import render
from pynput.mouse import Listener, Button
import cv2
from threading import Thread


def index(request):
    thread = Thread(target=start_listener)
    thread.start()
    return render(request, 'MouseTrackerApp/initial.html')


def take_photo():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Cannot open camera")
        return None

    ret, frame = camera.read()

    if ret:
        img_filename = 'captured_image.jpg'
        cv2.imwrite(img_filename, frame)
        print(f"Image captured and saved as {img_filename}")

    camera.release()
    return frame


def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        current_x, current_y = pyautogui.position()
        captured_frame = take_photo()

        print(f"Left button clicked at ({x}, {y}). Current position: ({current_x}, {current_y})")


def start_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()
