#this application using a webcamera as the input of yolo model

import cv2
from ultralytics import YOLO
from simple_pid import PID

# post request to move pioneer
def post_request(direction = 'right'):
    data = {
        'x': direction,
    }
    server_url = 'http://192.168.67.133:5000'
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        print(f"Action '{direction}' sent successfully.")
    else:
        print(f"Failed to send action '{direction}'. Server returned status code {response.status_code}")
    return 

# Returns the distance of the person from the centerline normed by the picture center line, >0=right, <0=left
# YOLOV8 docs for result attributes
def calculateDirection(results):
    if(results[0]):
        centerLine = 0.5
        bounding_box_coordinates = results[0].boxes[0].xywhn
        x_center = float(bounding_box_coordinates[0][0])
        distance = centerLine - x_center
        return distance
    else:
        return -1

pid = PID(1, 0.1, 0.05, setpoint=0)

#load the YOLOv8 model
model = YOLO('yolov8n.pt')

#open the video file
cap = cv2.VideoCapture(0)

#Loop through the video frames
while cap.isOpened():
    #Read a frame from the video
    success,frame = cap.read()

    if success:
        #Run YOLOv8 inference on the frame
        results = model(frame)
        # print(results[0])
        # cv2.waitKey(0)
        #Visuallize the results on the frame
        annotated_frame = results[0].plot()

        normDistance = calculateDirection(results)
        controllerOutput = pid(normDistance)

        annotated_frame = cv2.putText(annotated_frame, f"Distance: {round(normDistance, 5)}", (30,30), 1, 2, (0,0,255))
        annotated_frame = cv2.putText(annotated_frame, f"Control Value: {controllerOutput}", (30,60), 1, 2, (0,0,255))

        #Display the annotated frame
        cv2.imshow("YOLOv8 Inference",annotated_frame)

        #Break the loop if 'q' pressed
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        #else:
            #break the loop if the end of the video is reached
            #break
            #Release the video capture objec and close the display window

cap.release()
cv2.destroyAllWindows()
