import requests

def track_iphone(imei, serial):
    # Simulate a request to Apple's Find My iPhone service
    response = requests.get(f"https://findmyiphone.com/track?imei={imei}&serial={serial}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response for location data
        location_data = response.json()

        # Extract latitude and longitude coordinates
        latitude = location_data['latitude']
        longitude = location_data['longitude']

        print(f"iPhone 13 Location - Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Failed to track iPhone 13. Try again later.")

# Replace '123456789012345' with your iPhone 13's IMEI number
imei_number = '352678430510021'
# Replace 'ABC123456789' with your iPhone 13's serial number
serial_number = 'G3W3KHYF23'

# Call the function to track the iPhone 13
track_iphone(imei_number, serial_number)
