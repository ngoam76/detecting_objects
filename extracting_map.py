import requests
from urllib.parse import urlencode


api_key = "AIzaSyD06zFaNvB9VR8RiUrtwkVr0RX0nWmlnY0" # to access google maps data

# geocoding API
# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

def extract_lat_lng(address_or_postalcode, data_type = "json"):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}" #string
    params = {"address": address_or_postalcode, "key": api_key} # dictionary 
    url_params = urlencode(params) # encode dict into URL query string
    url = f"{endpoint}?{url_params}" # comebine two strings
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {} # dictionary
    latlng = {}
    try:
        latlng = r.json()["results"][0]["geometry"]["location"]
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")

# maps static API

# https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.998672&zoom=12&size=400x400&key=YOUR_API_KEY&signature=YOUR_SIGNATURE

# specifying locations from the center of created 4-point polygon
# creating paths based on these 4 points and display them on the created image of gg maps 

def plot_map(center_coord, map_zoom, map_size, map_path, map_type):
    endpoint = f"https://maps.googleapis.com/maps/api/staticmap" #string
    params = {"center": center_coord, "zoom": map_zoom, "size": map_size, "path": map_path, "maptype": map_type, "key": api_key} # dictionary 
    url_params = urlencode(params) # encode dict into URL query string
    url = f"{endpoint}?{url_params}" # comebine two strings
    return url
    




