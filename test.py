import requests
import base64

# 1. Read the local image and convert it to base64
with open("image.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

# 2. Send the POST request (Note: we use 127.0.0.1 here!)
url = "http://127.0.0.1:8080/"
payload = {"data": encoded_string}

try:
    print("Sending request...")
    response = requests.post(url, json=payload)

    # 3. Print the results
    print("Status Code:", response.status_code)
    print("Response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")
