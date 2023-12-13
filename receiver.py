from flask import Flask, request
import pyautogui

app = Flask(__name__)

def press_key(direction):
    pyautogui.press(direction)

@app.route('/', methods=['POST'])
def receive_pixel_coordinates():
    data = request.json
    x = data.get('x')
    y = data.get('y')

    if x is not None and y is not None:
        middle_pixel = 320  # Set your middle pixel value here

        if x < middle_pixel:
            # Press left button
            press_key('left')
            print("Left Button Pressed")
        elif x > middle_pixel:
            # Press right button
            press_key('right')
            print("Right Button Pressed")
        else:
            # Press forward button
            press_key('up')
            print("Forward Button Pressed")

    return "OK"

# Change the host parameter to '0.0.0.0' to allow external connections
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)
