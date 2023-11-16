import extracting_map
from shapely import wkt
from shapely.geometry import Polygon

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
lat_lng = center_point.replace("(", ")").replace(")", "").split(" ")

# define parameters for the function
center = f"{lat_lng[1]},{lat_lng[2]}"
zoom = "14"
size = "400x400"
print(extracting_map.plot_map(center, zoom, size))