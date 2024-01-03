import pyautogui
from pynput.mouse import Listener, Button
import cv2

def take_photo():
    # Initialize the camera (0 represents the default camera, change if you have multiple)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Cannot open camera")
        return None

    # Read a frame from the camera
    ret, frame = camera.read()

    if ret:
        # Save the captured frame as an image file
        img_filename = 'captured_image.jpg'  # Change the filename as needed
        cv2.imwrite(img_filename, frame)
        print(f"Image captured and saved as {img_filename}")

    # Release the camera
    camera.release()
    return frame


def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        current_x, current_y = pyautogui.position()
        captured_frame = take_photo()

        print(f"Left button clicked at ({x}, {y}). Current position: ({current_x}, {current_y})")


with Listener(on_click=on_click) as listener:
    listener.join()
