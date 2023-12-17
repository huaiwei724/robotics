import requests
import threading
def send_request_to_video_forget(direction):
    threading.Thread(target=send_request_to_video, args=(direction,)).start()


def send_request_to_video(message):
    port = 5001
    url = f'http://localhost:{port}' 
    payload = {"video": message}
    requests.post(url, json=payload)

if __name__ == "__main__":
    while True:
        user_input = input("Enter 1 to send a request to port 5001 or 'exit' to quit: ")

        if user_input == "1":
            send_request_to_video_forget('start')
        elif user_input == "0":
            send_request_to_video_forget('stop')
        else:
            print("Invalid input. Please enter '1' to send a request or 'exit' to quit.")
