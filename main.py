import extracting_map
from shapely import wkt
from shapely.geometry import Polygon
from flask import Flask, render_template, request, redirect, url_for

polygon_coords = []

def process_input(address1, address2, address3, address4, color, weight, zoom, size, maptype):
    address = [address1, address2, address3, address4]
    polygon_coords = []
    for i in address:
        polygon_coords.append(extracting_map.extract_lat_lng(i))
    
    # finding center point of 4 coords 
    polygon = Polygon(polygon_coords) # a list
    poly_wkt = polygon.wkt
    center_point = wkt.loads(f"{poly_wkt}").centroid.wkt
    lat_lng = center_point.replace("(", ")").replace(")", "").split(" ") # list

    coords_for_path = []
    # define path from 4 points
    for coord in polygon_coords:
        point_lat_lng = f"{coord[0]}, {coord[1]}"
        coords_for_path.append(point_lat_lng)
    path = f"color:{color}|weight:{weight}|{coords_for_path[0]}|{coords_for_path[1]}|{coords_for_path[2]}|{coords_for_path[3]}|{coords_for_path[0]}"

    # define parameters for the function
    center = f"{lat_lng[1]},{lat_lng[2]}"
    #print(extracting_map.plot_map(center, zoom, size, path))
    return str(extracting_map.plot_map(center, zoom, size, path, maptype))

# print(process_input("Blumenstraße, 80331 München", "Unterer Anger, 80331 München", "Müllerstraße, 80469 München", "Rumfordstraße, 80469 München", "red", "2", "15", "640x640", "satellite"))

#export to HTML
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Get form data
        # Addresses
        address1 = str(request.form['address1'])
        address2 = str(request.form['address2'])
        address3 = str(request.form['address3'])
        address4 = str(request.form['address4'])

        # Path parameters
        color = str(request.form['color'])
        weight = str(request.form['weight'])

        # Map parameters
        zoom = str(request.form['zoom'])
        size = str(request.form['size'])
        maptype = str(request.form['maptype'])

        # Process input by calling the function
        image_url = process_input(address1, address2, address3, address4, color, weight, zoom, size, maptype)

        # Render a template with the processed datax
        return render_template('index.html', image_url=image_url)
    
if __name__ == '__main__':
    app.run(debug=True, port=5500)