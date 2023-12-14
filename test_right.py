import requests
import time

# Set the server URL
server_url = 'http://127.0.0.1:5000'  # Change the IP address if needed

# Define the total duration and direction
total_duration_seconds = 15
direction = 'right'

# Keep track of the start time
start_time = time.time()

# Continue sending the 'right' action until the total duration is reached
while time.time() - start_time < total_duration_seconds:
    # Prepare the data payload
    data = {
        'x': direction,
        'y': None  # Assuming y coordinate is not needed for the 'right' action
    }

    # Send the POST request to the server
    response = requests.post(server_url, json=data)
    time.sleep(0.1)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Action '{direction}' sent successfully.")
    else:
        print(f"Failed to send action '{direction}'. Server returned status code {response.status_code}")
