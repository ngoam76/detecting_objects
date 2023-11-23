import extracting_map
from shapely import wkt
from shapely.geometry import Polygon
from flask import Flask, render_template

polygon_coords = []
# for i in range(4):
#     address = input(f"Enter the {i+1}. address: ")

address = ["Augustenstraße 92-94, 80798 München", "Augustenstraße 7, 80333 München", "Brienner Str. 11, 80333 München", "Schellingstraße 30, 80799 München"]

for i in address:
    polygon_coords.append(extracting_map.extract_lat_lng(i))

# finding center point of 4 coords 
polygon = Polygon(polygon_coords) # a list
poly_wkt = polygon.wkt
center_point = wkt.loads(f"{poly_wkt}").centroid.wkt
lat_lng = center_point.replace("(", ")").replace(")", "").split(" ") # list

coords_for_path = []
# define path from 4 points
color = "0xff0000ff"
weight = "5"
for coord in polygon_coords:
    point_lat_lng = f"{coord[0]}, {coord[1]}"
    coords_for_path.append(point_lat_lng)
path = f"color:{color}|weight:{weight}|{coords_for_path[0]}|{coords_for_path[1]}|{coords_for_path[2]}|{coords_for_path[3]}|{coords_for_path[0]}"

# define parameters for the function
center = f"{lat_lng[1]},{lat_lng[2]}"
zoom = "15"
size = "400x400" 
#print(extracting_map.plot_map(center, zoom, size, path))

#export to HTML
app = Flask(__name__)
@app.route('/')
def index():
    # Call the Python function
    image_url = str(extracting_map.plot_map(center, zoom, size, path))
    print(image_url)
    # Pass the image URL to the HTML template
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True, port=5500)