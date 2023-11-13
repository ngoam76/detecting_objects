import requests
from urllib.parse import urlencode

api_key = "AIzaSyD06zFaNvB9VR8RiUrtwkVr0RX0nWmlnY0" # to access google maps data
# geocoding API
def extract_lat_lng(address_or_postalcode, data_type = "json"):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key} # dictionary
    url_params = urlencode(params) # encode dict into URL query string
    url = f"{endpoint}?{url_params}" # comebine two strings
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    try:
        latlng = r.json()["results"][0]["geometry"]["location"]
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")

print(extract_lat_lng("174 Hung Vuong, Hue, Vietnam"))
#1600 Amphitheatre Parkway, Mountain View, CA