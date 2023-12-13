import cv2
import requests
import random
# Function to detect faces and get the middle pixel coordinates
def detect_face(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        # Take the first detected face
        x, y, w, h = faces[0]
        middle_x = x + w // 2
        middle_y = y + h // 2
        return middle_x, middle_y
    else:
        return None

# Function to send pixel coordinates through API
def send_pixel_coordinates(x, y):
    api_url = "http://127.0.0.1:5000/"  # Replace with your actual API endpoint
    payload = {"x": x, "y": y}
    requests.post(api_url, json=payload)

# Main loop to capture frames, detect faces, and send pixel coordinates
# cap = cv2.VideoCapture(0)  # 0 for default camera, you might need to change it

while True:
    #ret, frame = cap.read()
    # if not ret:
    #     break

    # face_coordinates = detect_face(frame)

    if False:#face_coordinates:
        x, y = face_coordinates
        send_pixel_coordinates(x, y)
    else:
        x=320+random.randint(-1,1)
        y=0
        send_pixel_coordinates(x, y)
        
    # cv2.imshow('Frame', frame)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# cap.release()
# cv2.destroyAllWindows()
