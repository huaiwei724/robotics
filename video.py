from flask import Flask, request
import cv2

app = Flask(__name__)

# Flag to control video playback
video_playing = False
video_path = r"C:\Users\Lakers\Downloads\big_buck_bunny_720p_1mb.mp4"
playback_position = 0


def play_video(video_path):
    global playback_position

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Set the window size to match the video resolution
    cv2.namedWindow("Video Player", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video Player", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    running = True
    current_frame = int(playback_position * fps)

    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    while running and video_playing:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video Player", frame)

        # Save the current playback position
        playback_position = cap.get(cv2.CAP_PROP_POS_FRAMES) / fps

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


@app.route('/', methods=['POST'])
def receive_pixel_coordinates():
    global video_playing

    data = request.json
    message = data.get('video')

    if message == 'start' and not video_playing:
        video_playing = True
        play_video(video_path)
    elif message == 'stop' and video_playing:
        video_playing = False

    return "OK"


# Change the host parameter to '0.0.0.0' to allow external connections
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
